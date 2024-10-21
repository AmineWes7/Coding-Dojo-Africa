
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Ninja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Ninja(db.Model):

    def update(self, name, age):
        self.name = name
        self.age = age
        db.session.commit()