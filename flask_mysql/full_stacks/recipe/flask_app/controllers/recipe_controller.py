from flask_app import app
from flask import render_template, session, redirect, request, flash

from flask_app.models.user import User
from flask_app.models.recipe import Recipe
# =====================================
# create recipe route
# ====================================

@app.route("/create")
def create():
    if "user_id" not in session: 
        flash("Please login or register before entering the site!")
        return redirect("/")

    return render_template("create.html")

# =====================================
# process recipe create route to create new recipe
# ====================================
@app.route("/new_recipe", methods = ["POST"])
def new_recipe():
    # 1. validate form data
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date" : request.form["date"],
        "under_thirty" : request.form["under_thirty"],

        "user_id" : session["user_id"],
    }
    if not Recipe.validate_recipe(data):
        return redirect("/new_recipe")

    Recipe.create_recipe(data)
    # 2.save new recipe to database
    # 3. redirect back to the dashboard page
    return redirect("/dashboard")
# ==================view one info
# ----------------------------

# ==================================
# view one recipe info
# ======================================
@app.route("/recipes/<int:recipe_id>/view")
def show_one(recipe_id):

    if "user_id" not in session: 
        flash("Please login or register before entering the site!")
        return redirect("/")
    data ={
        "recipe_id" : recipe_id
    }
    recipe = Recipe.get_recipe_user(data)
    print(recipe)
    return render_template("view.html", recipe = recipe)

# ====================================================
# edit recipe
# ===================================================
@app.route("/recipes/<int:recipe_id>/edit")
def edit(recipe_id):

    if "user_id" not in session: 
        flash("Please login or register before entering the site!")
        return redirect("/")
    data ={
        "recipe_id" : recipe_id
    }
    print(data)
    recipe = Recipe.get_recipe_user(data)
    return render_template("edit.html", recipe = recipe)

@app.route("/recipes/<int:recipe_id>/update", methods = ["POST"])
def update(recipe_id):
    # 1. validate form data
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "under_thirty" : request.form["under_thirty"],
        "date" : request.form["date"],

        "recipe_id" : recipe_id
    }
    print(data)
    if not Recipe.validate_recipe(data):
        return redirect(f"/recipes/{recipe_id}/edit")

    Recipe.update_recipe(data)
    # 2.save new recipe to database
    # 3. redirect back to the dashboard page
    return redirect("/dashboard")

@app.route("/recipes/<int:recipe_id>/delete")
def delete(recipe_id):

    data = {
        "recipe_id" : recipe_id
    }
    
    Recipe.delete_recipe(data)

    return redirect("/dashboard")