from src import db, login_manager
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask import abort
from typing import List

bcrypt = Bcrypt()

@login_manager.user_loader
def load_user(user_id): # セッションからIDを受け取り、ログインユーザーを返す
    return db.session.get(User, user_id)

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(64), unique=True)
    password: Mapped[str] = mapped_column(db.String(100), nullable=False)
    memos: Mapped[List["Memo"]] = relationship(back_populates="user")
    
    @classmethod
    def add_user(cls, username, email, password):
        hashed_password = bcrypt.generate_password_hash(password)
        user = cls(username=username, email=email, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500)
        return user

    @classmethod
    def select_by_email(cls, email):
        return cls.query.where(cls.email==email).one_or_none()
    
    @classmethod
    def select_by_username(cls, username):
        return cls.query.where(cls.username==username).one_or_none()
    
    def validate_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def change_password(self, new_password):
        hashed_password = bcrypt.generate_password_hash(new_password)
        self.password = hashed_password
        db.session.commit()
        return True
