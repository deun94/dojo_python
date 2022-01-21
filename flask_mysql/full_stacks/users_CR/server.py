from flask import Flask, render_template, redirect, session, request
from user import User
app = Flask(__name__)


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

if __name__=="__main__":
    app.run(debug=True)