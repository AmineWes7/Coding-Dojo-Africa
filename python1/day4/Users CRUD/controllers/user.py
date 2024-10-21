from flask import Flask, render_template, redirect, url_for, request
from models import init_db
from controllers import create_user, read_all_users, read_one_user, update_user, delete_user

app = Flask(__name__)

# Initialize the database
init_db()

@app.route("/")
def home():
    return redirect(url_for("read_all_users_route"))

@app.route("/users")
def read_all_users_route():
    users = read_all_users()
    return render_template("read_all_users.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def create_user_route():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        create_user(name, email)
        return redirect(url_for("read_all_users_route"))
    return render_template("create_user.html")

@app.route("/users/<int:id>")
def read_one_user_route(id):
    user = read_one_user(id)
    return render_template("read_one_user.html", user=user)

@app.route("/users/<int:id>/edit", methods=["GET", "POST"])
def edit_user_route(id):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        update_user(id, name, email)
        return redirect(url_for("read_one_user_route", id=id))
    
    user = read_one_user(id)
    return render_template("edit_user.html", user=user)

@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for("read_all_users_route"))

if __name__ == "__main__":
    app.run(debug=True)