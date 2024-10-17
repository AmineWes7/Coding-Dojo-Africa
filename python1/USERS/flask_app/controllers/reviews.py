from flask_app import app
from flask import render_template , request , redirect , session

from flask_app.models.review import Review
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if not 'logged_user_email' in session:
        return redirect('/')
    logged_user = User.get_by_email({'email': session['logged_user_email']})
    reviews = Review.get_all()
    return render_template('dashboard.html' , logged_user = logged_user , reviews = reviews)

@app.route('/reviews/new')
def add_review_page():
    if not 'logged_user_email' in session:
        return redirect('/')
    logged_user = User.get_by_email({'email': session['logged_user_email']})
    return render_template("add_review.html" , logged_user = logged_user)

@app.route('/reviews/create' , methods=['POST'])
def create_review():
    data = request.form
    Review.create(data)
    return redirect('/dashboard')

@app.route('/reviews/<int:id>/edit')
def edit_review_page(id):
    review = Review.get_by_id({'id': id})
    return render_template("edit_review.html" , review = review)


@app.route('/reviews/update' , methods=['POST'])
def update_review():
    data = request.form 
    Review.update(data)
    return redirect('/dashboard')

@app.route('/reviews/<int:id>/delete')
def delete_review(id):
    Review.delete({'id': id})
    return redirect('/dashboard')

@app.route('/reviews/<int:id>')
def show_review(id):
    review = Review.get_by_id({'id': id})
    return render_template("show_review.html" , review = review)