import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy import func, CheckConstraint

base_dir = os.path.dirname(__file__) # このファイルのディレクトリの絶対パス

app = Flask(__name__)

# データベース設定
database_path = os.path.join(base_dir, 'data_sqlalchemy1.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

db = SQLAlchemy(app)

# マイグレーション
Migrate(app, db, directory='data_sqlalchemy1')

# モデル
class Person(db.Model):
    __tablename__ = 'person'
    __table_args__ = (
        CheckConstraint('age >= 0', name='check_age_positive'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, default='不明')
    phone_number = db.Column(db.String(13), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(),
                           server_onupdate=func.now(), onupdate=datetime.now())
    
    def __str__(self):
        return f"id={self.id}, name={self.name}, age={self.age}"
