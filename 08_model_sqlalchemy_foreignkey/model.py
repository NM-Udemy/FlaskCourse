import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Employee(db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # One to Many
    projects = db.relationship('Project', backref='employees', lazy='dynamic')
    # One to One
    company = db.relationship('Company', backref='employees', uselist=False)

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        if self.company:
            return f"Employee name = {self.name} company is {self.company.name}"
        else:
            return f"Employee name = {self.name}, has no company"
    
    def show_projects(self):
        for project in self.projects:
            print(project.name)

class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # 外部キー
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Company(db.Model):

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

db.create_all()