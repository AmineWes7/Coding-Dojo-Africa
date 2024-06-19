from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dojos_and_ninjas'
db = SQLAlchemy(app)

class Dojo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Ninja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False)
    dojo = db.relationship('Dojo', backref=db.backref('ninjas', lazy=True))

@app.route('/dojos')
def dojos():
    dojos = Dojo.query.all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/new', methods=['GET', 'POST'])
def new_dojo():
    if request.method == 'POST':
        dojo = Dojo(name=request.form['name'])
        db.session.add(dojo)
        db.session.commit()
        return redirect(url_for('dojos'))
    return render_template('new_dojo.html')

@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    dojo = Dojo.query.get(dojo_id)
    return render_template('dojo_show.html', dojo=dojo)

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.query.all()
    return render_template('ninjas.html', dojos=dojos)

@app.route('/ninjas/new', methods=['GET', 'POST'])
def new_ninja():
    if request.method == 'POST':
        dojo_id = int(request.form['dojo_id'])
        ninja = Ninja(first_name=request.form['first_name'], last_name=request.form['last_name'], dojo_id=dojo_id)
        db.session.add(ninja)
        db.session.commit()
        return redirect(url_for('dojo_show', dojo_id=dojo_id))
    dojos = Dojo.query.all()
    return render_template('new_ninja.html', dojos=dojos)

if __name__ == '__main__':
    app.run(debug=True)