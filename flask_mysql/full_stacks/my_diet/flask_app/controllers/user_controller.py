from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def mainpage():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods = ["POST"])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "pass_conf" : request.form["pass_conf"]
    }

    if not User.validate_user(data):
        return redirect("/register")
    
    print(request.form["password"])
    
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)

    data["password"] = pw_hash

    new_user_id = User.create_user(data)

    session["user_id"] = new_user_id


    return redirect ("/")


@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/login_user", methods = ["POST"])
def login_user():
    data={
        "email" : request.form["email"],
        "password" : request.form["password"]
    }

    if not User.validate_login(data):
        return redirect("/login")
    


    user = User.get_by_email(data)
    # 3.save user info in session
    session["user_id"] = user.id

    return render_template("dashboard.html")


# ====================================
# logout
# =======================
@app.route("/logout")
def logout():
    session.clear()
    flash("Succesfully logged out!")
    return redirect("/")