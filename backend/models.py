from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(50), default='user')
