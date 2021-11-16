# __ init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config.settings import DevelopmentConfig, ProductionConfig

login_manager = LoginManager() # Flask-Loginライブラリとアプリケーションをつなぐ
# ログインの関数
login_manager.login_view = 'app.login'
# ログインにリダイレクトした際のメッセージ
login_manager.login_message = 'ログインしてください'


basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

config = {
    'development': 'config/development/settings.cfg',
    'production': 'config/production/settings.cfg'
}
config_class = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

def create_app():
    app = Flask(__name__) 
    # config_file = config[os.getenv('ENVIRONMENT', 'development')]
    # app.config.from_pyfile(config_file)
    # print(f'config_file = {config_file}')
    ## 環境変数を直接指定
    # app.config.from_envvar('FLASK_CONFIG_ENV')
    
    # クラスから読み込む
    config_target = config_class[os.getenv('ENVIRONMENT', 'development')]
    app.config.from_object(config_target)

    from flaskr.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app
