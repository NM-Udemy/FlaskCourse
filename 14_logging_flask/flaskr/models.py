# models.py
from flaskr import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app

# セッションに保存されたログインユーザを返すためにtemplateから呼ばれる
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# UserMixinはFLask-Loginライブラリを利用するユーザが持つべきオブジェクトを定義
class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        is_password_valid = check_password_hash(self.password, password)
        if not is_password_valid:
            current_app.logger.warning('パスワードが誤っています')
        return is_password_valid

    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()
    
    @classmethod
    def select_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
