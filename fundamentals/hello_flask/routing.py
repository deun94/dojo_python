from flask import Flask

app = Flask (__name__)

@app.route("/")

def Hello_world():
    return "Hello World!"

@app.route("/dojo")

def Hello_dojo():
    return "Dojo!"

@app.route("/say/<str:name>")

def say_hi(name):
    print(name)
    return "Hi " + name

@app.route("/repeat/<int:num>/<str:word>")

def repeat(num, word):
    newWord = num * word
    return f"Repeating {newWord}"

if __name__=="__main__":
    app.run(debug = True)
