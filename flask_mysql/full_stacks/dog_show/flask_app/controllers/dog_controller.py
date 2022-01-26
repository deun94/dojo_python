from flask_app import app

from flask import render_template, redirect, request, session, flash
from flask_app.models.owner import Owner
from flask_app.models.dog import Dog

# =====================================
# create dog route
# ====================================

@app.route("/new_dog")
def new_dog():
    if "owner_id" not in session: 
        flash("Please login or register before entering the site!")
        return redirect("/")

    return render_template("new_dog.html")
    # or owner_id = session["owner_id"]

# =====================================
# process dog route
# ====================================
@app.route("/create_dog", methods = ["POST"])
def create_dog():
    # don't be passing owner id to the url
    # session owner id

    # 1. validate form data
    data = {
        "name" : request.form["name"],
        "breed" : request.form["breed"],
        "age" : request.form["age"],

        # "owner_id" : request.form["owner_id"]
        "owner_id" : session["owner_id"],
        # or pull owner_id : session["owner_id"] rather than passing it in 
        # at the new dog route
    }
    if not Dog.validate_dog(data):
        return redirect("/new_dog")

    Dog.create_dog(data)
    # 2.save new dog to database
    # 3. redirect back to the dashboard page
    return redirect("/dashboard")

# =========================================
# Show one dog route
# ======================================
@app.route("/dog/<int:dog_id>")
def show_dog(dog_id):
    # checking for logged in
    if "owner_id" not in session: 
        flash("Please login or register before entering the site!")
        return redirect("/")
    # 1. query for dog info w/associated info of owner

    data={
        "dog_id" : dog_id
    }
    dog = Dog.get_dog_with_owner(data)

    return render_template("show_dog.html", dog = dog)

# ====================
# edit
# ===================
@app.route("/dog/<int:dog_id>/edit")
def edit_dog(dog_id):
    # query for the dog we want to update
    # which is the same for the get_dog_by_id

    data ={
        "dog_id" : dog_id
    }
    dog = Dog.get_dog_with_owner(data)

    # pass the dog info to the html
    return render_template("edit_dog.html", dog = dog)

@app.route("/dog/<int:dog_id>/update", methods = ["POST"])
def update_dog(dog_id):
    # 1. validate form data
    data = {
        "name" : request.form["name"],
        "breed" : request.form["breed"],
        "age" : request.form["age"],
        # still need the dog id
        "dog_id" : dog_id
    }

    if not Dog.validate_dog(data):
        return redirect(f"/dog/{dog_id}/edit")
    # update form information

    Dog.update_dog_info(data)


    return redirect("/dashboard")

# ======================
# delete one dog route
# ===============
@app.route("/dog/<int:dog_id>/delete")
def delete_dog(dog_id):

    data = {
        "dog_id" : dog_id
    }

    Dog.delete_dog_info(data)

    return redirect("/dashboard")