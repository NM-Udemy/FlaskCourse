from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)
Migrate(app, db)

class Member(db.Model):
    __tablename__ = 'member'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(128))
    age: Mapped[int] = mapped_column(db.Integer)
    comment: Mapped[str] = mapped_column(db.String(255), nullable=True)
