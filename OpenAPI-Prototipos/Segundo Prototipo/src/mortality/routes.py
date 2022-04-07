from flask import request, Response, Blueprint
import pymongo, json
from bson import ObjectId, json_util

#connection to Database
try:
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017, 
        serverSelectionTimeoutMS = 1000
        )
    db = mongo.datos_abiertos_2012_2020
    mongo.server_info()#trigger exception if not able to connect to db
except:
    print("ERROR - Cannot connect to DataBase")

#defining the  Blueprint
mortalidad = Blueprint("mortalidad", __name__, url_prefix='/mortality/v.1')

#region API Endpoints

#main GET endpoint
@mortalidad.route('/main', methods=['GET'])
def main():
    try:
        dead = list(db.mortalidad.find({"anio_ocur" : 2012, "escolarida" : 2, "ent_ocurr" : 10}))
        dead = json.dumps(dead, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= dead,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        return Response(
            response= json.dumps({ "message" : "impossible to access /main URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-state" GET endpoint
@mortalidad.route('/mortality-state', methods=['GET'])
def get_mortality_state():
    try:
        #catching values
        state = request.args.get("state", default=0, type=int)

        data = list(db.mortalidad.find({"ent_ocurr" : state}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-state URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-state-year" GET endpoint
@mortalidad.route('/mortality-state-year', methods=['GET'])
def get_mortality_state_year():
    try:
        #catching values
        state = request.args.get("state", default=0, type=int)
        year = request.args.get("year", default=0, type=int)

        data = list(db.mortalidad.find({"ent_ocurr" : state, "anio_ocur" : year}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-state-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-scholarship-year" GET endpoint
@mortalidad.route('/mortality-scholarship-year', methods=['GET'])
def get_scholarship_year():
    try:
        #catching values
        scholarship = request.args.get("scholarship", default=0, type=int)
        year = request.args.get("year", default=0, type=int)

        data = list(db.mortalidad.find({"anio_ocur" : year, "escolarida" : scholarship}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-scholarship-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-scholarship-state" GET endpoint
@mortalidad.route('/mortality-scholarship-state', methods=['GET'])
def get_scholarship_state():
    try:
        #catching values
        scholarship = request.args.get("scholarship", default=0, type=int)
        state = request.args.get("state", default=0, type=int)

        data = list(db.mortalidad.find({"ent_ocurr" : state, "escolarida" : scholarship}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-scholarship-state URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-sex-year" GET endpoint
@mortalidad.route('/mortality-sex-year', methods=['GET'])
def get_sex_year():
    try:
        #catching values
        sex = request.args.get("sex", default=0, type=int)
        year = request.args.get("year", default=0, type=int)

        data = list(db.mortalidad.find({"sexo" : sex, "anio_ocur" : year}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-sex-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-sex-state" GET endpoint
@mortalidad.route('/mortality-sex-state', methods=['GET'])
def get_sex_state():
    try:
        #catching values
        sex = request.args.get("sex", default=0, type=int)
        state = request.args.get("state", default=0, type=int)

        data = list(db.mortalidad.find({"sexo" : sex, "ent_ocurr" : state}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-sex-state URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-medical-year" GET endpoint
@mortalidad.route('/mortality-medical-year', methods=['GET'])
def get_medical_year():
    try:
        #catching values
        medical = request.args.get("medical", default=0, type=int)
        year = request.args.get("year", default=0, type=int)

        #validate values
        data = list(db.mortalidad.find({"asist_medi" : medical, "anio_ocur" : year}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-medical-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-morbidity" GET endpoint
@mortalidad.route('/top-enfermedades', methods=['GET'])
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

#endregion

#coder Class for ObjectID Type
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)