from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def survey_response():

    data = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }

    if not User.validate_user(data):
        return redirect("/")

    new_user_id = User.create_user(data)
    return redirect('/')

# @app.route('/result')
# def show_result():

#     return render_template('result.html')