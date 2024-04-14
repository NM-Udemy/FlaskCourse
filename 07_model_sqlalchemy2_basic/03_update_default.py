from models import app, db, Person

with app.app_context():
    try:
        person = db.session.get(Person, 1)
        person.name="Jiro"
        person.age=25
        db.session.commit()
    except Exception as e:
        db.session.rollback()
