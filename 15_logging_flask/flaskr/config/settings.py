import os

class DevelopmentConfig:
    basedir = os.path.abspath(os.path.dirname(__name__))
    SECRET_KEY='mysite'
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ENV='development'


class ProductionConfig:
    basedir = os.path.abspath(os.path.dirname(__name__))
    SECRET_KEY='mysite'
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ENV='production'