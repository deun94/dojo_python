from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def survey_response():

    data = {
        session["name"] : request.form["name"],
        session["location"] : request.form["location"],
        session["gender"] : request.form["gender"],
        session["language"] : request.form["language"],
        session["comment"] : request.form["comment"]
    }

    if not User.validate_user(data):
        return redirect("/")

    user = User.create_user(data)

    return redirect('/result')

@app.route('/result')
def show_result():


    return render_template('result.html')