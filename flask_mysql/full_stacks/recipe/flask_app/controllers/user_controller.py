from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/")
def index():
    return render_template("index.html")

# ====================================================
# register user
# ===================================================

@app.route("/new_user", methods=["POST"])
def register_user():

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "pass_conf" : request.form["pass_conf"]
    }

    if not User.validate_user(data):
        return redirect("/")
    
    print(request.form["password"])
    
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)

    data["password"] = pw_hash

    new_user_id = User.create_user(data)

    session["user_id"] = new_user_id

    return redirect("/dashboard")

# =============================================
# login then redirect to dashboard
# ============================================
@app.route("/login", methods = ["POST"])
def login():
    # 1.validate login info
    data={
        "email" : request.form["email"],
        "password" : request.form["password"]
    }

    if not User.validate_login(data):
        return redirect("/")
    

    # 2. query for user info based on email
    user = User.get_by_email(data)
    # 3.save user info in session
    session["user_id"] = user.id

    return redirect("/dashboard")

# =====================================
# render dashboard route
# ====================================

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session: 
        flash("Please login or register before entering the site!")
        return redirect("/")

    data = {
        "user_id" : session["user_id"]
    }
    user = User.get_by_id(data)
    all_recipes = Recipe.get_all_recipes()
    # recipes = Recipe.get_user_with_recipes(data)
    return render_template("dashboard.html", user = user, all_recipes = all_recipes)

# ====================================
# logout
# =======================
@app.route("/logout")
def logout():
    session.clear()
    flash("Succesfully logged out!")
    return redirect("/")