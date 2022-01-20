from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)






if __name__=="__main__":
    app.run(debug=True)