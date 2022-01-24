from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    dojos = Dojo.show_all()
    print(dojos)
    for dojo in dojos:
        print(dojo.name)

    return render_template("index.html")