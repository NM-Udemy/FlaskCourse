from models import app, db, Person
from datetime import datetime

with app.app_context():
    specific_datetime = datetime(2023, 1, 1, 12, 0, 0)
    try:
        new_person = Person(name="Taro", phone_number="080-0000-0000", age=30, 
                            created_at=specific_datetime, updated_at=specific_datetime)
        db.session.add(new_person)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
