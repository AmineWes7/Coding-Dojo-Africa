from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection details
mydb = mysql.connector.connect(
host="localhost",
user="your_username",
password="your_password",
database="your_database"
)

# Create a cursor object
mycursor = mydb.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]

    # Insert the new user into the database
    sql = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
    val = (first_name, last_name, email)
    mycursor.execute(sql, val)
    mydb.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)