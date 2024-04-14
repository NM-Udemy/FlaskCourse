from models import Person, db, app
import time
from sqlalchemy import update, delete
from werkzeug.exceptions import NotFound

with app.app_context():
    # person = Person.query.get_or_404(1)
    # print(person)
    # person.age += 1
    # db.session.commit()
    # print(Person.query.get_or_404(1))
    # sql = update(Person).where(
    #     Person.id==1
    # ).values(age=Person.age+1)
    # # print(sql)
    # db.session.execute(sql)
    # db.session.commit()
    # print(Person.query.get_or_404(1))
    print(db.session.execute(
        db.Select(Person.age).where(Person.name=='鈴木 千代')
    ).fetchall())
    sql = update(Person).where(
        Person.name == '鈴木 千代'
    ).values(
        age=Person.age+1
    )
    # db.session.execute(sql)
    # db.session.commit()
    
    print(db.session.execute(
        db.Select(Person.age).where(Person.name=='鈴木 千代')
    ).fetchall())
    
    
    print(db.session.execute(
        db.Select(Person.age).where(Person.age>75)
    ).fetchall())
    # db.session.delete(person)
    sql = delete(Person).where(Person.age>75)
    print(sql)
    db.session.execute(sql)
    db.session.commit()
    print(db.session.execute(
        db.Select(Person.age).where(Person.age>75)
    ).fetchall())