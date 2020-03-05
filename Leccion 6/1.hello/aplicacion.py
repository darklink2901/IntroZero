from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, world!!!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/maria")
def maria():
    return "Hello, Maria!"

@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"

app.run(port=5000, debug=True)
