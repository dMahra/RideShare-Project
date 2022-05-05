from os import abort

from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

from models import db, Vehicles
# from WebApp.models import Vehicles

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
                con.execute("PRAGMA read_uncommitted = true;");
                print('entered')
                cur = con.cursor()
                # prepared statement for 'Customer' table insertion
                query = 'INSERT INTO Customer (Name, Cur_address, Phone_number, Password) VALUES (:Name,:Address,:Phone_Number,:Password)'
                cur.execute(query, JsonVals)
                # cur.execute('INSERT INTO Customer (Name, Cur_address, Phone_number, Password) VALUES (?,?,?,?)',
                #             (Name, Address, str(Phone_Number), Password))
                con.commit()
                quotes = '"'
                sqltemp = "SELECT Customer_id from Customer WHERE Name =" +quotes+ str(Name)+ quotes + \
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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");

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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");
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
                con.execute("PRAGMA read_uncommitted = true;");
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


@app.route('/vehicle/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('registerVehicle.html')

    if request.method == 'POST':
        vehicle_id = request.form['vehicle_id']
        state = request.form['state']
        licensePlateNumber = request.form['licensePlateNumber']
        make = request.form['make']
        vehicle = Vehicles(vehicle_id=vehicle_id, state=state, licensePlateNumber=licensePlateNumber, make=make)
        db.session.add(vehicle)
        db.session.commit()
        return redirect('/vehicle')

@app.route('/vehicle')
def RetrieveList():
    vehicles = Vehicles.query.all()
    return render_template('vehicleList.html',vehicles = vehicles)

@app.route('/vehicle/<int:id>')
def RetrieveVehicle(id):
    vehicle = Vehicles.query.filter_by(vehicle_id=id).first()
    if vehicle:
        return render_template('vehicle.html', vehicle = vehicle)
    return "Vehicle with id: " + str(id) + "Doesn't exist"


@app.route('/vehicle/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    vehicle = Vehicles.query.filter_by(vehicle_id=id).first()
    if request.method == 'POST':
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            state = request.form['state']
            licensePlateNumber = request.form['licensePlateNumber']
            make = request.form['make']
            vehicle = Vehicles(vehicle_id=id, state=state, licensePlateNumber=licensePlateNumber, make=make)
            db.session.add(vehicle)
            db.session.commit()
            return redirect('/vehicle/' + str(id))
        return "Vehicle with id: " + str(id) + "Doesn't exist"

    return render_template('vehicleUpdate.html', vehicle=vehicle)


@app.route('/vehicle/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    vehicle = Vehicles.query.filter_by(vehicle_id=id).first()
    if request.method == 'POST':
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return redirect('/vehicle')
        abort(404)

    return render_template('vehicleDelete.html')

if __name__ == '__main__':
    app.run(debug=True)