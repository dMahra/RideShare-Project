from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicles(db.Model):
  __tablename__ = 'vehicles'
  id=db.Column(db.Integer, primary_key=True,unique = True)
  vehicle_id = db.Column(db.Integer(), unique = True)
  state = db.Column(db.String(50))
  licensePlateNumber = db.Column(db.Integer())
  make = db.Column(db.String(50))
  def __init__(self,vehicle_id,state,licensePlateNumber,make):
    self.vehicle_id = vehicle_id
    self.state = state
    self.licensePlateNumber = licensePlateNumber
    self.make = make
  def __repr__(self):
      return "vehicle id: " + str(self.vehicle_id)


# @app.route('/vehicle/create' , methods = ['GET','POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('registerVehicle.html')
 
#     if request.method == 'POST':
#         vehicle_id = request.form['vehicle_id']
#         state= request.form['state']
#         licensePlateNumber = request.form['licensePlateNumber']
#         make = request.form['make']
#         vehicle = Vehicles(vehicle_id=vehicle_id,state=state,licensePlateNumber=licensePlateNumber,make=make)
#         db.session.add(vehicle)
#         db.session.commit()
#         return redirect('/registered')

# @app.route('/vehicle')
# def RetrieveList():
#     vehicles = Vehicles.query.all()
#     return render_template('vehicleList.html',vehicles = vehicles)

# @app.route('/vehicle/<int:id>')
# def RetrieveEmployee(id):
#     vehicle = Vehicles.query.filter_by(vehicle_id=id).first()
#     if vehicle:
#         return render_template('vehicle.html', vehicle = vehicle)
#     return f"Vehicle with id ={id} Doesn't exist"

# @app.route('/vehicle/<int:id>/update',methods = ['GET','POST'])
# def update(id):
#     vehicle = Vehicles.query.filter_by(vehicle_id=id).first()
#     if request.method == 'POST':
#         if vehicle:
#             db.session.delete(vehicle)
#             db.session.commit()
#             vehicle_id = request.form['vehicle_id']
#             state= request.form['state']
#             licensePlateNumber = request.form['licensePlateNumber']
#             make = request.form['make']
#             vehicle = Vehicles(vehicle_id=vehicle_id,state=state,licensePlateNumber=licensePlateNumber,make=make)
#             db.session.add(vehicle)
#             db.session.commit()
#             return redirect(f'/vehicle/{id}')
#         return f"Vehicle with id = {id} Doesn't exist"
 
#     return render_template('vehicleUpdate.html', vehicle = vehicle)

# @app.route('/vehicle/<int:id>/delete', methods=['GET','POST'])
# def delete(id):
#     vehicle = Vehicles.query.filter_by(vehicle_id=id).first()
#     if request.method == 'POST':
#         if vehicle:
#             db.session.delete(vehicle)
#             db.session.commit()
#             return redirect('/vehicle')
#         abort(404)
 
#     return render_template('vehicleDelete.html')
 