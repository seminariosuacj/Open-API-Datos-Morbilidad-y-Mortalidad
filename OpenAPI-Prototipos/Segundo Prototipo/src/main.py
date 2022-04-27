from app import create_app

app = create_app()

#auto debug on save
if __name__ == '__main__':
    app.run(debug=True)








































""""

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



        """