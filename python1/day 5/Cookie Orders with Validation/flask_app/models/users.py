from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CookieOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cookie_type = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<CookieOrder {self.name} - {self.cookie_type}>'