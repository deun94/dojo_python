from flask import Flask, render_template
# import the class from user.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all users
    # need the method call to match the one you are importing from
    users = User.get_all()
    print(users)
    for user in users:
        print(user.first_name)
    return render_template("index.html", users = users)

@app.route('/<int:user_id>')
def one_User(user_id):

    data = {
        'user_id': user_id
    }
    user = User.one_user(data)
    print(user)
    return render_template('info.html', user =user)


if __name__ == "__main__":
    app.run(debug=True)

#