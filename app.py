from flask import flask

app = Flask(__name__)   

@app.route("/hello ")
def hello():
    return "Olá, mundo"