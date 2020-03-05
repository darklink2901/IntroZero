import random #importar random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    variablerandom = random.choice(["Hello, world!", "Hi there!", "Good morning!"])
    return render_template("index.html", headline=variablerandom)
