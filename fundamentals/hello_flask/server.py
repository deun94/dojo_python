from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world() :
    # return "Hello World!"
    return render_template("hello.html", phrase = "hello", times = 5)

@app.route("/success")
def success():
    return "Success"

# @app.route("/hello/<str:name>/<int:num>")
# def hello(name, num):
#     # print(name)
#     # return "Hello, " + name
#     return render_template("hello.html", name = "Adrien", num = num)

@app.route("/users/<username>/<id>")
# two parameters username and id
def show_user_profile(username, id) : 
    print (username)
    print(id)
    return "username: " + username + ", id:" + id


if __name__=="__main__":
    app.run(debug = True)

