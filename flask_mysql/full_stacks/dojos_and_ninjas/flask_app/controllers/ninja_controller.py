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
        "dojo_id" : request.form["dojo_id"],
        # the key needs to match the passing in data 
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }

    Ninja.add_ninja(data)
    

    return redirect("/dojos")
    # remember it's not = , it is key : value

@app.route("/<int:ninja_id>/edit")
def edit_ninja(ninja_id):

    data = {
        "ninja_id" : ninja_id
    }

    ninja = Ninja.get_ninja_with_dojo(data)

    return render_template("edit_ninja.html", ninja = ninja)

@app.route("/<int:ninja_id>/update", methods = ["POST"])
def update_ninja(ninja_id):

    dojos = Dojo.show_all()

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age": request.form["age"],

        "ninja_id" : ninja_id
    }

    
    Ninja.update_ninja(data)


    return redirect("/dojos", dojos = dojos)

@app.route("/<int:ninja_id>/delete")
def delete_ninja(ninja_id):

    data = {
        "ninja_id" : ninja_id
    }

    Ninja.delete_ninja(data)

    return redirect("/dojos")
