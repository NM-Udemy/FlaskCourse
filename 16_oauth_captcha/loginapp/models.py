from loginapp import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
import string
import random


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def __init__(self, email, username=None, password=None):
        self.email = email
        self.username = username
        if password is None:
            letters = string.ascii_lowercase
            password = ''.join(random.choice(letters) for _ in range(10))
        self.password = generate_password_hash(password)

    @classmethod
    def select_by_email(cls, email):
        return cls.query.filter(cls.email==email).first()
    
    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def validate_password(self, password):
        return check_password_hash(self.password, password)
