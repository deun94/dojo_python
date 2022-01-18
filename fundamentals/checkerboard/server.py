from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/x/y')
def x_y(x, y):
    row = int(x)
    column = int(y)
    return render_template('checkerboard.html', row=row, coloum=column)





if __name__=="__main__":
    app.run(debug=True)