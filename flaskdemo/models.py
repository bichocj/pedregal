from db import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    mother_last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    