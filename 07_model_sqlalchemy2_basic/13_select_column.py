from models import Person, db, app
import time

with app.app_context():
    sql = db.Select(Person.id, Person.name)
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print(persons[0])
    print(persons[0].id)
    print(persons[0].name)

    # Label追加
    sql = db.Select(Person.id.label("person_id"), Person.name.label('person_name'))
    persons = db.session.execute(sql).fetchone()
    print(persons.person_id)
    print(persons.person_name)
    
    print('-' * 100)
    sql = db.Select(Person)
    sql = sql.with_only_columns(Person.id, Person.name)
    
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print(persons[0])
    print(persons[0].id)
    print(persons[0].name)
    
    
    sql = db.Select(Person)
    sql = sql.with_only_columns(Person.id.label('person_id'), Person.name.label('person_name'))
    
    print(sql)
    persons = db.session.execute(sql).fetchmany(10)
    print(persons[0])
    print(persons[0].person_id)
    print(persons[0].person_name)
