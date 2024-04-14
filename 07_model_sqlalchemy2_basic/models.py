import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy import func, CheckConstraint

base_dir = os.path.dirname(__file__) # このファイルのディレクトリの絶対パス

app = Flask(__name__)

# データベース設定
database_path = os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

# SQLAlchemyのベースクラス
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

# マイグレーション設定
Migrate(app, db) # appとdbを渡して、flask dbが実行できるようにする

# モデルの定義
class Person(db.Model):
    __tablename__ = 'person'
    __table_args__ = (
        CheckConstraint('age >= 0', name='check_age_positive'),
    )
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, index=True, default='不明')
    phone_number: Mapped[str] = mapped_column(db.String(13), nullable=False, unique=True) # NOT NULL, UNIQUE
    age: Mapped[int] = mapped_column(db.Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now(),
                                                 server_onupdate=func.now(), onupdate=datetime.now())
    
    def __str__(self):
        return f"id={self.id}, name={self.name}, age={self.age}"
