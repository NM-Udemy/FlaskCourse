from models import Person, db, app
import time
from sqlalchemy import and_, or_, func

def show_result(sql):
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print([str(person[0]) for person in persons])

with app.app_context():
    sql = db.Select(func.count(Person.id).label('person_count'))
    person = db.session.execute(sql).fetchone()
    print(person.person_count)
    sql = db.Select(
        func.max(Person.age).label('max_age'), func.min(Person.age).label('min_age'),
        func.sum(Person.age).label('sum_age')
    ).where(and_(Person.id>20, Person.id<30))
    print(sql)
    person = db.session.execute(sql).fetchone()
    print(person.min_age)