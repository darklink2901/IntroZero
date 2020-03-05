from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    variableenindex = "Hello, world informatico!"
    return render_template("index.html", headline=variableenindex)

@app.route("/bye")
def bye():
    variablebye = "Goodbye!"
    return render_template("index.html", headline=variablebye)
