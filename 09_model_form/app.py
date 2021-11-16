# model-exam/app.py
import os
from flask import Flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__name__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
