from flask_app import app
from flask import session , request , render_template , redirect
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register' , methods=['POST'])
def register():
    data = request.form
    if User.validate_register(data):
        User.register(data)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        session['logged_user_email'] = data['email']
        # Redirect to the protected route
        return redirect('/dashboard')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')