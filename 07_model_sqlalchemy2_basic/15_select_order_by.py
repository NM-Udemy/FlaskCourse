from models import Person, db, app
import time
from sqlalchemy import and_, or_

def show_result(sql):
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print([str(person[0]) for person in persons])

with app.app_context():
    sql = db.Select(Person).order_by(Person.age.desc(), Person.id.desc())
    show_result(sql)
    sql = db.Select(Person.name, Person.id, Person.age).where(
        Person.id<20).order_by(
        Person.age.desc()
    )
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print(persons[0].id)
    print(persons[0].name)
    print(persons[0].age)
    