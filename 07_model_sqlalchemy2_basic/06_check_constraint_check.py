from models import app, db, Person

with app.app_context():
    try:
        person = Person(name='John', age=-10, phone_number="111-1111-1111")
        db.session.add(person)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
