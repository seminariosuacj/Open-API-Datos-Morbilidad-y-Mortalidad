from operator import le


try:
    from flask import request, Response, Blueprint
    import pymongo, json
    from bson import ObjectId, json_util
    from marshmallow import Schema, fields, validates, ValidationError
    from http.client import BAD_REQUEST
    from flask_restful import abort
    from marshmallow import validates
    from bson import SON
except Exception as e:
    print("Some Modules are missing {}".format(e))

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
        #state = reqArgs.validate(request.args)

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
    #validate Arguments
    try:
        #validate the request args
        schema = StateYearSchema()
        errors = schema.validate(request.args)
    except ValidationError as err:
        print(errors)
        return Response(
            response= json.dumps(err.valid_data),
            status=400,
            mimetype="application/json"
        )
    #Retrieve information
    try:
        #catching values
        state = request.args.get("state", type=int)
        year = request.args.get("year", type=int)

        #Querying the data
        data = list(db.mortalidad.find({"ent_ocurr" : state, "anio_ocur" : year}))

        #Decodify data from List to JSON
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)

        #returning JSON Data with Response obj
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
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
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-medical-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-age-range" GET endpoint
@mortalidad.route('/mortality-age-range', methods=['GET'])
def get_age_ranges():
    try:
        #catching values
        age = request.args.get("age", default=0, type=int)
        data = list(db.mortalidad.find({"edad_agru" : age}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-sex-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/mortality-age-range-year" GET endpoint
@mortalidad.route('/mortality-age-range-year', methods=['GET'])
def get_age_ranges_year():
    try:
        #catching values
        age = request.args.get("age", default=0, type=int) 
        year = request.args.get("year", default=0, type=int)
        data = list(db.mortalidad.find({"edad_agru" : age, "anio_ocur" : year}))
        data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        return Response(
            response= json.dumps({ "message" : "impossible to access /mortality-sex-year URI" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-morbidity" GET endpoint
@mortalidad.route('/top-morbidity', methods=['GET'])
def get_top_morbidity():
    try:
        data = morbidity()
        data = json.dumps(data)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-morbidity-year" GET endpoint
@mortalidad.route('/top-morbidity-year', methods=['GET'])
def get_top_morbidity_year():
    try:
        year = request.args.get("year", default=0, type=int)
        data = morbidity_year(year)
        #data = json.dumps(data, cls=JSONEncoder, default=json_util.default)
        data = json.dumps(data)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-mortality-states" GET endpoint
@mortalidad.route('/top-mortality-states', methods=['GET'])
def get_top_mortality_states():
    try:
        data = mortality_state()
        data = json.dumps(data)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#"/top-mortality-states-year" GET endpoint
@mortalidad.route('/top-mortality-states-year', methods=['GET'])
def get_top_mortality_states_year():
    try:
        year = request.args.get("year", default=0, type=int)
        data = mortality_state_year(year)
        data = json.dumps(data)
        return Response(
            response= data,
            status= 200,
            mimetype= "application/json"
        )
    except Exception as ex:
        return Response(
            response= json.dumps({ "message" : "cannot get users" } ),
            status=500,
            mimetype="application/json"
        )

#endregion

#region Query Functions for TOP URI's
#top-morbidity query function
def morbidity():
    pipeline = [
        { "$unwind" : "$lista_mex"},
        { "$group" : {"_id" : "$lista_mex", "count" : { "$sum" : 1} } },
        { "$sort" : SON([ ("count", -1), ("_id", -1) ]) }
    ]
    morb = list(db.mortalidad.aggregate(pipeline))
    top_morb = morb[:10]
    return top_morb

#top-morbidity-year query function
def morbidity_year(year):
    pipeline = [
        { "$match" : {"anio_ocur" : year}},
        { "$unwind" : "$lista_mex"},
        { "$group" : {"_id" : "$lista_mex", "count" : { "$sum" : 1} } },
        { "$sort" : SON([ ("count", -1), ("_id", -1) ]) }
    ]
    morb = list(db.mortalidad.aggregate(pipeline))
    top_morb = morb[:10]
    #data = []
    #for i in top_morb:
        #data.append(list(db.mortalidad.find({"anio_ocur" : year, "lista_mex" : i["_id"]})))
    #print(len(data))
    return top_morb

#top-mortality-states query function
def mortality_state():
    pipeline = [
        { "$unwind" : "$ent_ocurr"},
        { "$group" : {"_id" : "$ent_ocurr", "count" : { "$sum" : 1} } },
        { "$sort" : SON([ ("count", -1), ("_id", -1) ]) }
    ]
    morb = list(db.mortalidad.aggregate(pipeline))
    top_morb = morb[:10]
    return top_morb

#top-mortality-states-year query function
def mortality_state_year(year):
    pipeline = [
        { "$match" : {"anio_ocur" : year}},
        { "$unwind" : "$ent_ocurr"},
        { "$group" : {"_id" : "$ent_ocurr", "count" : { "$sum" : 1} } },
        { "$sort" : SON([ ("count", -1), ("_id", -1) ]) }
    ]
    morb = list(db.mortalidad.aggregate(pipeline))
    top_morb = morb[:10]
    #data = []
    #for i in top_morb:
        #data.append(list(db.mortalidad.find({"anio_ocur" : year, "lista_mex" : i["_id"]})))
    #print(len(data))
    return top_morb
#endregion

#coder Class for ObjectID Type
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

#serialization Classes for args validation
#Class for State and Year args
class StateYearSchema(Schema):
    state = fields.Integer(required= True)
    year = fields.Integer(required= True)

    @validates('state')
    def state_valid(self, value):
        valid_ranges = list(range(1, 35))
        valid_ranges.append(99)
        if not value in valid_ranges:
            raise ValidationError("'state' not in valid range, check Documentation")
    
    @validates('year')
    def year_valid(self,value):
        valid_range = list(range(2012, 2020))
        if not value in valid_range:
            raise ValidationError("'year' not in valid range, chech Documentation")