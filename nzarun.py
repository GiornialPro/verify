from nza import app

app.config.from_mapping(secret_key='merdatoda222', DEBUG=True)
app.config["SESSION_PERMANET"] = False
app.config["SESSION_TYPE"] = "filesystem"

if __name__ == "__main__":
    # app.run()
    app.run( host='0.0.0.0', port='80')
    # app.run( host='horarius.zapto.org', port='80')
    # app.run( host='105.172.30.78', port='80')