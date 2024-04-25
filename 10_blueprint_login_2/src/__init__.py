from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from .models import Base

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysite"
    
    base_dir = os.path.dirname(__file__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    
    db.init_app(app)
    db.model_class = Base
    Migrate(app, db)
    
    login_manager.init_app(app)
    login_manager.login_view = 'account.login'
    
    from src.main import main_bp
    from src.account import account_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(account_bp)
    
    return app
