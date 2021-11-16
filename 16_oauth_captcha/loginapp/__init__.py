import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_dance.contrib.google import make_google_blueprint
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha


login_manager = LoginManager()
login_manager.login_message = 'ログインしてください'

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

google_blueprint = make_google_blueprint(
    client_id="134737185015-krn23hukblb5u2mul5ni9eepmt946rd4.apps.googleusercontent.com",
    client_secret="3IaoCm-HWTgbSeM2RnjQOqr9",
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
    redirect_to='app.google_login'
)

from uuid import uuid4

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(uuid4())
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CAPTCHA_ENABLE'] = True
    app.config['CAPTCHA_LENGTH'] = 5
    app.config['CAPTCHA_WIDTH'] = 160
    app.config['CAPTCHA_HEIGHT'] = 100
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    Session(app)
    captcha = FlaskSessionCaptcha(app)
    app.register_blueprint(google_blueprint, url_prefix='/login')
    from loginapp.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app
