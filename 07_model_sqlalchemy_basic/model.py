# models2/model.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, CheckConstraint

base_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Person(db.Model):

    __tablename__ = 'persons'
    __table_args__ = (
        CheckConstraint('update_at >= create_at'), # チェック制約
    )
    id = db.Column(db.Integer, primary_key=True) # 主キー
    name = db.Column(db.String(20), index=True, server_default='nanashi') # デフォルト値
    phone_number = db.Column(db.String(13), nullable=False, unique=True) # NOT NULL, UNIQUE
    age = db.Column(db.Integer, nullable=False) # NOT NULL
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)

    def __init__(self, name, phone_number, age, create_at, update_at):
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.create_at = create_at
        self.update_at = update_at
    
    def __str__(self):
        return f"id = {self.id}, name={self.name}, phone_number={self.phone_number}, age={self.age}, create_at={self.create_at}, update_at={self.update_at}"

db.Index("my_index", func.lower(Person.name)) # lower(name)

db.create_all()