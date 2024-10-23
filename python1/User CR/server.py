from flask import Flask, render_template, redirect, request, session
from user_model import User

app = Flask(__name__)
app.secret_key = "My Secrete Key"

@app.route('/users')
def index():
    # calling the get_all method from the friends.py
    all_users=User.get_all()
    # passing all friends to our template so we can display them there
    return render_template("index.html", users=all_users)

@app.route("/users/new")
def create():
    return render_template("create_user.html")

@app.route("/users/create", methods=['POST'])
def user_submit():
    User.save(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
