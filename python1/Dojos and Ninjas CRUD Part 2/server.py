from flask import render_template
from flask_app.models.users import Users
from flask_app.models.app import app

def read_all_users():
    users = User.get_all_users()
    return render_template("users.html", users=users)