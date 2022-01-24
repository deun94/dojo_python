from flask_app import app
from flask import render_template, request, session, redirect

@app.route("/ninjas")
def addNinja():
    return render_template("add_ninja.html")