from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas/add")

def newNinja():

    dojos = Dojo.show_all()
    ninjas = Ninja.get_ninja()

    return render_template("add_ninja.html", dojos = dojos, ninjas = ninjas)

@app.route("/add_ninja", methods =["POST"])

def add_ninja():

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }

    Ninja.add_ninja(data)
    

    return redirect("/dojos")
    # remember it's not = , it is key : value
