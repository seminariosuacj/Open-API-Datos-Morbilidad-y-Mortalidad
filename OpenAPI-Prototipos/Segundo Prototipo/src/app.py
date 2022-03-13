#required packages
from flask import Flask, Response, request
import json
import pymongo
app = Flask (__name__)

#auto debug on save
if __name__ == "__main__":
    app.run(debug=True)

#connection to Database
try:
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017, 
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.datos_abiertos_2012_2020
    mongo.server_info()#trigger exception if not able to connecto to db
except:
    print("ERROR - Cannot connecto to DataBase")

#"/top-morbidity" GET endpoint
@app.route('/top-enfermedades', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json con top 10 enfermedades del 2012-2020"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-morbidity-year" GET endpoint
@app.route('/top-enfermedades-year', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json con top 10 enfermedades por año"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/state-casualties" GET endpoint
@app.route('/state-casualties', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json para las muertes de un determinado estado del 2012 - 2020"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-state-year" GET endpoint
@app.route('/mortality-state-year', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json para las muertes de un determinado estado por año"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-scholarship" GET endpoint
@app.route('/mortality-scholarship', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json para las muertes por escolaridad por año"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-scholarship-state" GET endpoint
@app.route('/mortality-scholarship-state', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json para las muertes por escolaridad por estado 2020-2012"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-sex" GET endpoint
@app.route('/mortality-sex', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json para las muertes por sexo 2020-2012"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-sex-year" GET endpoint
@app.route('/mortality-sex-year', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json para las muertes por sexo de un determinado año"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-comorbidity" GET endpoint
@app.route('/top-comorbidity', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json top co-morbilidaes 2012-2020"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-medical-attention" GET endpoint
@app.route('/mortality-medical-attention', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json Mortalidad y atención médica"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-top-states" GET endpoint
@app.route('/mortality-top-states', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json Estados con mayor índice de mortalidad"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-age-ranges" GET endpoint
@app.route('/mortality-age-ranges', methods=['GET'])
def get_top_enfermedades():
    try:
        data = "json Mortalidad por rangos de edad"
        return data
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )