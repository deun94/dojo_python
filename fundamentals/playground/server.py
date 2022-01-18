from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def index():
    return "go to /play for boxes"

@app.route("/play")
def blue_block():
    return render_template("repeat.html", num = 3, color = "skyblue")

@app.route("/play/<int:num>")
def repeat_block(num):
    return render_template("repeat.html", num = num, color = "skyblue")

@app.route("/play/<int:num>/<string:color>")
def num_and_color(num, color):
    return render_template("repeat.html", num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)