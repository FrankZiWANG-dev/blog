from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.String(20000))
    date = db.Column(db.DateTime, default=func.now())
    image = db.Column(db.Text(), unique=True, nullable=False)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    text = db.Column(db.String(20000))
    date = db.Column(db.DateTime, default=func.now())
    link = db.Column(db.String(1000))