from flask import Flask, render_template, request, session
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "whatever"
app.permanent_session_lifetime=timedelta(minutes=1) 

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = [] 

    if request.method == "POST": 
        session.permanent=True 
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"]) 
