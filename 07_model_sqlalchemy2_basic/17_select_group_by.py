from models import Person, db, app
import time
from sqlalchemy import and_, or_, func

def show_result(sql):
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print([str(person[0]) for person in persons])

with app.app_context():
    sql = db.Select(
        Person.age, func.count(Person.id).label('id_count'),
        func.max(Person.id).label('id_max')
    ).where(Person.id>=500).group_by(
        Person.age
    ).order_by(func.count(Person.id).desc())
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print(persons)
    print(persons[0].age)
    print(persons[0].id_count)
    print(persons[0].id_max)
