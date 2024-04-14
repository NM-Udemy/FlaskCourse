from models import app, db, Person

with app.app_context():
    try:
        person = Person(id=1, name="John", phone_number="080-1111-1111", age=30)
        db.session.add(person)
        db.session.commit()
    except Exception as e:
        # print(e)
        db.session.rollback()
    try:
        person1 = Person(name="John", phone_number="080-2222-2222", age=30)
        person2 = Person(name="Mike", phone_number="080-2222-2222", age=20)
        db.session.add(person1)
        db.session.add(person2)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
