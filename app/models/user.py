from database import db

class User(db.Model):
    __tablename__ = 'users'
    identifier_number = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
