from application import app

@app.route("/")
def abc():
    return "<h1>Hello</h1>"
    
@app.route("/index")
def index():
    return "<h1>Hello This is my First Flask app</h1>"