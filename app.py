from flask import Flask, render_template, request
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
            Name = request.form['name']
            Address = request.form['address']
            Phone_Number = request.form['pn']
            Password = request.form['password']

            # print(Name, Address, Phone_Number, Password)

            with sql.connect('Uber.db') as con:
                print('entered')
                cur = con.cursor()
                cur.execute('INSERT INTO Customer (Name, Cur_address, Phone_number, Password) VALUES (?,?,?,?)',
                            (Name, Address, str(Phone_Number), Password))
                con.commit()
                message = "successfully added"
        except Exception as e:
            print(e)
            con.rollback()
            message = "error in operation"
        finally:
            con.close()
            return render_template("results.html", msg=message)


if __name__ == '__main__':
    app.run(debug=True)
