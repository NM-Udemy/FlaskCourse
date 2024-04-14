from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask import Flask
from typing import List

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

database_path = os.path.join(base_dir, 'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'company'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(128))
    employees: Mapped[List["Employee"]] = relationship(back_populates="company")


class Employee(db.Model):
    __tablename__ = 'employee'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(128))
    company_id: Mapped[int] = mapped_column(db.ForeignKey("company.id"))
    company: Mapped["Company"] = relationship(back_populates="employees")


class User(db.Model):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(128), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(128), unique=True, nullable=False)
    
    profile: Mapped["Profile"] = relationship(back_populates="user")

class Profile(db.Model):
    __tablename__ = 'profile'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), unique=True)
    full_name: Mapped[str] = mapped_column(db.String(128), nullable=False)
    location: Mapped[str] = mapped_column(db.String(128))
    
    user: Mapped["User"] = relationship(back_populates="profile")
    
class BookAuthor(db.Model):
    __tablename__ = "book_author"
    book_id: Mapped[int] = mapped_column(db.ForeignKey("book.id"), primary_key=True)
    author_id: Mapped[int] = mapped_column(db.ForeignKey("author.id"), primary_key=True)
    book: Mapped["Book"] = relationship(back_populates="book_authors")
    author: Mapped["Author"] = relationship(back_populates="book_authors")
        
class Book(db.Model):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    book_name: Mapped[str] = mapped_column(db.String(128))
    book_authors: Mapped[List["BookAuthor"]] = relationship(back_populates="book")

class Author(db.Model):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(db.String(128))
    book_authors: Mapped[List["BookAuthor"]] = relationship(back_populates="author")
    
