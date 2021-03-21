import mysql.connector
import json
from flask import Flask, render_template, request, jsonify, Response, json  # import flask        
app = Flask(__name__)             # create an app instance

@app.route("/getMakes", methods=['GET'])                   # at the end point /getMakes to get the makes models and submodels
def getMakes():                      # call method getMakes
    cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              port='3306',
                              database='project_schema')
    cur = cnx.cursor()
    cur.execute('''Select * from cars c  join makes ma on c.make_id=ma.id join models mo on c.model_id=mo.id join submodels smo on c.submodel_id=smo.id;''')
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
    return response
    #http://127.0.0.1:5000/getMakes

@app.route("/getCars", methods=['GET'])                   # at the end point /getCars to get the cars
def getCars():                      # call method getCars
    cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              port='3306',
                              database='project_schema')
    cur = cnx.cursor()
    cur.execute('select make_id,model_id,submodel_id from cars;')
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
    return response
    #http://127.0.0.1:5000/getCars

@app.route("/insertCar", methods=['GET'])                   # at the end point /insertCar to insert car
def insertCar():                # call method insertCar
    cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              port='3306',
                              database='project_schema')
    car_id = request.args.get("carid")
    active = request.args.get("active")
    year = request.args.get("year")
    mileage = request.args.get("mileage")
    price = request.args.get("price")
    make_id = request.args.get("makeid")
    model_id = request.args.get("modelid")
    submodel_id = request.args.get("submodelid")
    body_type = request.args.get("bodytype")
    transmission = request.args.get("transmission")
    fuel_type = request.args.get("fueltype")
    exterior_color = request.args.get("exteriorcolor")
    cur = cnx.cursor()
    cur.execute('''insert into cars
values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','2018-06-15 09:40:16+02','2018-06-15 09:40:16+02'
,null);'''.format(car_id,active,year,mileage,price,make_id,model_id,submodel_id,body_type,transmission,fuel_type,exterior_color))
    cnx.commit()
    return("Added successfully!")
    #http://127.0.0.1:5000/insertCar?carid=testCar&active=t&year=2017&mileage=72000&price=124000&makeid=toyota&modelid=71&submodelid=1266&bodytype=SUV&transmission=Automatic&fueltype=petrol&exteriorcolor=white

@app.route("/getCertainCars", methods=['GET'])                   # at the end point /getMakes to get the certain cars
def getCertainCars():                      # call method getCertainCars
    cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              port='3306',
                              database='project_schema')
    priceStart = request.args.get("priceStart")
    priceEnd = request.args.get("priceEnd")
    mileageStart = request.args.get("mileageStart")
    mileageEnd = request.args.get("mileageEnd")
    cur = cnx.cursor()
    cur.execute('''Select * from cars Where Price between {} AND {} AND Mileage between {} AND {} ORDER BY updated_at ASC;'''.format(priceStart, priceEnd, mileageStart, mileageEnd))
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result))) #Pack the results into json format

    response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
    return response
    #http://127.0.0.1:5000/getCertainCars?priceStart=70000&priceEnd=200000&mileageStart=30000&mileageEnd=70000


if __name__ == "__main__":
     #Connect to the database server
    app.run()





