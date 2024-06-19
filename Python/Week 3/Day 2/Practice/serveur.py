from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
app.secret_key = 'ecret_key'

bcrypt = Bcrypt(app)

# MySQL database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='login_registration'
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    errors = []

    if not first_name.isalpha() or len(first_name) < 2:
        errors.append('First name must be at least 2 characters and contain only letters')
    if not last_name.isalpha() or len(last_name) < 2:
        errors.append('Last name must be at least 2 characters and contain only letters')
    if not email:
        errors.append('Email is required')
    elif not validate_email(email):
        errors.append('Invalid email format')
    elif check_email_exists(email):
        errors.append('Email already exists in the database')
    if len(password) < 8:
        errors.append('Password must be at least 8 characters')
    if password!= confirm_password:
        errors.append('Passwords do not match')

    if errors:
        return render_template('index.html', errors=errors)
    else:
        hashed_password = bcrypt.generate_password_hash(password)
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, hashed_password))
        db.commit()
        session['user_id'] = cursor.lastrowid
        return redirect(url_for('success'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    errors = []

    if not email:
        errors.append('Email is required')
    elif not validate_email(email):
        errors.append('Invalid email format')
    if not password:
        errors.append('Password is required')

    if errors:
        return render_template('index.html', errors=errors)
    else:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user and bcrypt.check_password_hash(user[3], password):
            session['user_id'] = user[0]
            return redirect(url_for('success'))
        else:
            errors.append('Invalid email or password')
            return render_template('index.html', errors=errors)

@app.route('/success')
def success():
    if 'user_id' in session:
        return render_template('success.html')
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def validate_email(email):
    if '@' in email and '.' in email:
        return True
    return False

def check_email_exists(email):
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True)