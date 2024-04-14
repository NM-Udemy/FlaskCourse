from models import app, db, Person
from datetime import datetime

with app.app_context():
    specific_datetime = datetime(2023, 1, 1, 12, 0, 0)
    try:
        default_person = Person(phone_number="080-1111-1111", age=30)
        db.session.add(default_person)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
