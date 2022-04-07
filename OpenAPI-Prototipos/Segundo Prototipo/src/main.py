from app import create_app

app = create_app()

#auto debug on save
if __name__ == '__main__':
    app.run(debug=True)








































""""



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
        """