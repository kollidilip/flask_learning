from flask import Flask


app = Flask(__name__)


@app.route("/")
def abc():
    return "<h1>Hello</h1>"
    
@app.route("/index")
def index():
    return "<h1>Hello This is my First Flask app</h1>"
