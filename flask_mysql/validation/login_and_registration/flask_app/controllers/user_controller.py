from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_user", methods=["POST"])
def create_user():

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"]

    }

    if not User.validate_user(data):
        return redirect("/")
    
    print(request.form["password"])
    
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)

# update the password field of our data object to be the hashed password in our database
    data["password"] = pw_hash
    # we do all this  BEFORE creating our user data
    # makesure password field at our schema is varchar(455) because we need long enuf storage
    new_user_id = User.create_user(data)

    session["user_id"] = new_user_id
    # call on session, name it user_id, 
    # redirect the information to the dashbord to save the session
    return redirect("/dashboard")

@app.route("/login", methods = ["POST"])
def login():
    # see if the provided input is existing in the database
    data = {
        "email" : request.form["email"],
        "password" : request.form["password"]
    }

    # validate FROM data
    if not User.validate_login(data):
        return redirect("/")
        # if not match, return to the homepage
    
    # "log in" user
    logged_in_user = User.get_by_email(data)
# quering from your user
    session["user_id"] = logged_in_user.id

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    # personalizing the dashboard depending on who is logging in
    if "user_id" not in session:
        flash("Please login/register before entering the site!")
        return redirect("/")
    # if you try to enter this route w.o entering a proper login info, it will flash error

    data = {
        "user_id" : session["user_id"]
    }
    # grabbing the ssession of the input upon login

    user = User.get_user_by_id(data)
    # also need the classmethod to get user by id

# remember to pass in the user! 
    return render_template("dashboard.html", user = user)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
