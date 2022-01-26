from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.show_all()
    print(dojos)
    for dojo in dojos:
        print(dojo.name)

    return render_template("index.html", dojos=dojos)
    # have to pass in the info to show 

# =====================================
# show one dojo
# ========================================

@app.route("/dojos/<int:dojo_id>")
def dojo_with_ninjas(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }

    dojos_with_ninjas = Dojo.get_dojo_with_ninjas(data)

    # print(dojo)

    return render_template("show_dojo.html", dojo = dojos_with_ninjas)


# ===========================================
# create new dojo
# =========================================
@app.route("/new_dojo", methods = ["POST"])
def new_dojo():
    data = {
        "name" : request.form["name"]
    }

    Dojo.add_dojo(data)
    

    return redirect("/dojos")