from models import Person, db, app
import time
from sqlalchemy import and_, or_, func

def show_result(sql):
    print(sql)
    persons = db.session.execute(sql).fetchmany(100)
    print([str(person[0]) for person in persons])

with app.app_context():
    sql = db.Select(Person.name).order_by(Person.name).distinct()
    show_result(sql)

    sql = db.Select(Person).offset(2).limit(2)
    show_result(sql)
    
    sql = db.Select(Person).where(Person.age>75).offset(2000).limit(2)
    show_result(sql)
    