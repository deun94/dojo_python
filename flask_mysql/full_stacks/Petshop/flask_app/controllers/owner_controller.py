from flask import render_template, redirect, session, request
from flask_app import app
# don't need to import flask because we have that in the __init__py
# app = Flask(__name__)
from flask_app.models.owner import Owner
# from the owner file import owner class

@app.route('/')
def index():

    owners_with_pets = Owner.owners_with_pets()
    return render_template('index.html', owners = owners_with_pets)


@app.route("/<int:owner_id>")
def show_one_user(owner_id):
    data={
        "owner_id" : owner_id
    }

    one_owner = Owner.get_one_user(data)
    return render_template("show.html", owner=one_owner)


# if __name__=="__main__":
#     app.run(debug=True)