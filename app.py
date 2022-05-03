from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/customers')
def new_customer():
    return render_template('customer.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            # Customer_id = request.form['Customer_id']
            Name = request.form['name']
            Address = request.form['address']
            Phone_Number = request.form['pn']
            Password = request.form['password']
            #
            JsonVals = {"Name": Name, "Address": Address, "Phone_Number": Phone_Number, "Password": Password}

            # print(Name, Address, Phone_Number, Password)

            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                # prepared statement for 'Customer' table insertion
                query = 'INSERT INTO Customer (Name, Cur_address, Phone_number, Password) VALUES (:Name,:Address,:Phone_Number,:Password)'
                cur.execute(query, JsonVals)
                # cur.execute('INSERT INTO Customer (Name, Cur_address, Phone_number, Password) VALUES (?,?,?,?)',
                #             (Name, Address, str(Phone_Number), Password))
                con.commit()
                quotes = '"'
                sqltemp="SELECT Customer_id from Customer WHERE Name =" +quotes+ str(Name)+ quotes + \
                        "and Cur_address =" +quotes+ str(Address)+ quotes + "and Password =" +quotes+ str(Password)+ quotes+ \
                        "and Phone_number =" +Phone_Number
                cur.execute(sqltemp)
                temp= cur.fetchall()
                message = "successfully added new customer with id: " + str(temp[len(temp)-1][0])
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation" #+ str(Customer_id)
        finally:
            con.close()
            return render_template("results.html", msg=message)


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    print(request.method)
    if request.method == 'POST':
        try:
            # print(request.form['Customer_id'])

            with sql.connect('RideShare.db') as con:
                cur = con.cursor()
                quotes = '"'
                sqltemp = "DELETE from Customer WHERE Password =" + quotes + str(request.form['password']) + quotes + "and Customer_id =" + request.form['Customer_id']
                cur.execute(sqltemp)
                message = "successfully removed new Customer with id: " + str(request.form['Customer_id'])


        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("results.html", msg=message)
    else:
        try:
            print(request.form)
            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                print(request)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)
        finally:
            con.close()
            return render_template("login.html")



@app.route('/driver')
def new_driver():
    return render_template('driver.html')



@app.route('/adddriver', methods=['POST', 'GET'])
def adddriver():
    print(request.method)
    if request.method == 'POST':
        try:
            # Driver_id = request.form['Drive_id']
            Name = request.form['name']
            Birthday = request.form['birthday']
            Phone_Number = request.form['pn']
            Password = request.form['password']
            Car_id = request.form['carid']
            JsonVals = {"Name": Name, "Phone_Number": Phone_Number, "Birthday": Birthday, "Password": Password,
                        "Car_id": Car_id}

            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                # prepared statement for 'Driver' table insertion
                query = 'INSERT INTO Driver (Name, Birthday, Phone_number, Password, Car_id) VALUES (:Name,:Birthday,:Phone_Number,:Password,:Car_id)'
                cur.execute(query, JsonVals)
                # cur.execute('INSERT INTO Driver (Name, Phone_Number, Birthday, Password, Car_id) VALUES (?,?,?,?,?)',
                #             (Name, str(Phone_Number), Birthday, Password, Car_id))
                con.commit()
                quotes = '"'
                sqltemp = "SELECT Drive_id from Driver WHERE Name =" + quotes + str(Name) + quotes + \
                          " and Birthday =" + quotes + str(Birthday) + quotes + " and Password =" + quotes + str(
                    Password) + quotes +  " and Phone_number =" + Phone_Number +  " and Car_id =" + Car_id
                cur.execute(sqltemp)
                temp = cur.fetchall()
                message = "successfully added new driver with id: " + str(temp[len(temp) - 1][0])
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"
        finally:
            con.close()
            return render_template("results.html", msg=message)
    else:
        return render_template('driver.html')

@app.route('/driverlogin', methods=['GET', 'POST'])
def driverlogin():
    error = None
    print(request.method)
    if request.method == 'POST':
        try:
            # print(request.form['Customer_id'])

            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                quotes = '"'
                sqltemp = "DELETE from Driver WHERE Password =" + quotes + str(request.form['password']) + quotes + "and Drive_id =" + request.form['Drive_id']
                cur.execute(sqltemp)
                message = "successfully removed new Driver with id: " + str(request.form['Drive_id'])
                print(message)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("results.html", msg=message)
    else:
        try:
            print(request.form)
            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                print(request)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("driverlogin.html")

@app.route('/driverupdate', methods=['GET', 'POST'])
def driverupdate():
    error = None
    print(request.method)
    if request.method == 'POST':
        try:
            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                quotes = '"'
                sqltemp = "UPDATE Driver SET Password =" + quotes + str(request.form['newpassword']) + quotes + "WHERE Drive_id =" + request.form['Drive_id'] + " AND Password =" + quotes + str(request.form['oldpassword']) + quotes
                cur.execute(sqltemp)
                message = "successfully Changed password for Driver with id: " + str(request.form['Drive_id'])
                print(message)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("results.html", msg=message)
    else:
        try:
            print(request.form)
            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                print(request)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("driverupdate.html")

@app.route('/customerupdate', methods=['GET', 'POST'])
def customerupdate():
    error = None
    print(request.method)
    if request.method == 'POST':
        try:
            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                quotes = '"'
                sqltemp = "UPDATE Customer SET Password =" + quotes + str(request.form['newpassword']) + quotes + "WHERE Customer_id =" + request.form['Customer_id'] + " AND Password =" + quotes + str(request.form['oldpassword']) + quotes
                cur.execute(sqltemp)
                message = "successfully Changed password for Customer with id: " + str(request.form['Customer_id'])
                print(message)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("results.html", msg=message)
    else:
        try:
            print(request.form)
            with sql.connect('RideShare.db') as con:
                print('entered')
                cur = con.cursor()
                print(request)
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"  # + str(Customer_id)

        finally:
            con.close()
            return render_template("customerupdate.html")

if __name__ == '__main__':
    app.run(debug=True)
