from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    for user in users:
        print(user.first_name)
    return render_template('read.html', users = users)


# ====================================
# going to create page with form 
# =============================
@app.route("/create")
def create():
    return render_template("create.html")


# ================================
# adding a user
# ================================

@app.route("/add_user", methods=["POST"])
def add_user():
    # 1 - collect the info from the form

    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
    }
    # 3 - call on query
    new_user_id = User.create_user(data)

    # 4 - if successful, redirect to a render route
    return redirect("/")


# ==============================
# showing one user actions
# ===========================

@app.route('/<int:user_id>')
def one_User(user_id):
    data = {
        'user_id': user_id
    }
    user = User.one_user(data)
    print(user)
    return render_template('show.html', user = user)

# ================================================
# edit info
# ================================================

# when edit it clicked ===========================

@app.route("/<int:user_id>/edit")

def edit_User(user_id):
    data = {
        'user_id': user_id
    }
    user = User.one_user(data)
    # need to see it first /the computer
    print(user)
    return render_template("edit.html", user=user)

# ===============================================
# goes to edit page

@app.route("/edit_user/<int:user_id>", methods=["POST"])
# int this is LABELING the data transferred from the url from the html page
def edit_user(user_id):
    data = {
        "user_id" : user_id,
        # to specify which user
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
    }
    # 3 - call on query
    # user_id = User.edit_user(data)
    User.edit_user(data)
    # editing you don't really need to save here 그냥 고치는거

    # 4 - if successful, redirect to a render route
    return redirect("/")
    
# ================================================
# delete info
# ================================================

@app.route("/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        'user_id': user_id
    }
    user = User.delete_user(data)
    print(user)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
