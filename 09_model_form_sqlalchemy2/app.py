import os
from flask import Flask

app = Flask(__name__)
basedir = os.path.dirname(__file__)

database_path = os.path.join(basedir, 'data.sqlite')

app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
