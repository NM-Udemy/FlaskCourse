from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_dance.contrib.google import make_google_blueprint
import os
from .models import Base

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysite"
    app.config["GOOGLE_OAUTH_CLIENT_ID"] = ""
    app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = ""
    
    base_dir = os.path.dirname(__file__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    app.config["RECAPTCHA_PUBLIC_KEY"] = ''
    app.config["RECAPTCHA_PRIVATE_KEY"] = ''
    
    db.init_app(app)
    db.model_class = Base
    Migrate(app, db)
    
    login_manager.init_app(app)
    login_manager.login_view = 'account.login'
    
    from src.main import main_bp
    from src.account import account_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(account_bp)
    
    google_bp = make_google_blueprint(
        scope=["profile", "email"],
        redirect_to='account.google_login',
    )
    app.register_blueprint(google_bp, url_prefix="/google_login")
    
    return app
