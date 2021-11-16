# models.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
Migrate(app, db)

class Member(db.Model):

    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    comment = db.Column(db.Text)

    def __init__(self, name, age, comment):
        self.name = name
        self.age = age
        self.comment = comment
