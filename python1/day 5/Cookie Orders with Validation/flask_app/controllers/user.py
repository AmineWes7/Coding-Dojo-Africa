# app.py
from flask import Flask, render_template, redirect, url_for, flash
from models import db, CookieOrder
from forms import CookieOrderForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cookie_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    orders = CookieOrder.query.all()
    return render_template('order_list.html', orders=orders)

@app.route('/cookies/new', methods=['GET', 'POST'])
def create_order():
    form = CookieOrderForm()
    if form.validate_on_submit():
        new_order = CookieOrder(
            name=form.name.data,
            cookie_type=form.cookie_type.data,
            number=form.number.data
        )
        db.session.add(new_order)
        db.session.commit()
        flash('Order created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_order.html', form=form)

@app.route('/cookies/edit/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = CookieOrder.query.get_or_404(order_id)
    form = CookieOrderForm(obj=order)
    if form.validate_on_submit():
        order.name = form.name.data
        order.cookie_type = form.cookie_type.data
        order.number = form.number.data
        db.session.commit()
        flash('Order updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_order.html', form=form, order=order)

@app.route('/cookies/delete/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = CookieOrder.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    flash('Order deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)