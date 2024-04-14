from models import Person, db, app
import time
from sqlalchemy import and_, or_

def show_result(sql):
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print([str(person[0]) for person in persons])

with app.app_context():
    sql = db.Select(Person).where(Person.id < 10)
    show_result(sql)
    show_result(db.Select(Person).where(Person.name == "鈴木 千代"))
    
    # 複数条件(and, or)
    show_result(db.Select(Person).where(and_(
        Person.name == "鈴木 千代", Person.age > 50)))
    show_result(db.Select(Person).where(or_(
        Person.age < 25, Person.age > 75
    )))
    show_result(db.Select(Person).where(Person.name.like('%田%')))
    show_result(db.Select(Person).where(Person.id.in_([1,2,3])))
    
    sql = db.Select(Person).where(Person.name == "鈴木 千代")
    start_time = time.time()
    db.session.execute(sql).fetchone()
    end_time = time.time()
    print('Exection time: ', end_time - start_time)
    