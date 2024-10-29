from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def is_valid(self):
        if not self.first_name or not self.last_name or not self.email:
            flash("Please fill in all fields", "error")
            return False


        import re
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, self.email):
            flash("Please enter a valid email address", "error")
            return False

        return True



@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request