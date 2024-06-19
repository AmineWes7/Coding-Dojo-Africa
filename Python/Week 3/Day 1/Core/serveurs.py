from flask import Flask, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/dojos_and_ninjas_schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Dojo and Ninja models
# ...

# Define schema for Dojo and Ninja
# ...

# Define routes
# ...

if __name__ == '__main__':
    app.run(debug=True)
    -----------------------------------------------------------
    class Dojo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    ninjas = db.relationship('Ninja', backref='dojo', lazy=True)

class Ninja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False)
    ---------------------------------------------------------
    @app.route('/dojos', methods=['GET'])
def get_dojos():
    dojos = Dojo.query.all()
    dojo_schema = DojoSchema(many=True)
    return dojo_schema.jsonify(dojos)

@app.route('/dojos/<int:id>', methods=['GET'])
def get_dojo(id):
    dojo = Dojo.query.get(id)
    dojo_schema = DojoSchema()
    return dojo_schema.jsonify(dojo)

@app.route('/dojos', methods=['POST'])
def add_dojo():
    name = request.json['name']
    address = request.json['address']
    dojo = Dojo(name=name, address=address)
    db.session.add(dojo)
    db.session.commit()
    dojo_schema = DojoSchema()
    return dojo_schema.jsonify(dojo)

@app.route('/ninjas', methods=['GET'])
def get_ninjas():
    ninjas = Ninja.query.all()
    ninja_schema = NinjaSchema(many=True)
    return ninja_schema.jsonify(ninjas)