from models import Person, db, app
import time
from sqlalchemy import and_, or_, func
from werkzeug.exceptions import NotFound

with app.app_context():
    try:
        person = Person.query.get_or_404(10000)
        print(person)
    except NotFound as e:
        print(e)
    
    person = Person.query.where(Person.name=='鈴木 千代').first_or_404()
    print(person)
    
    try:
        person = Person.query.where(Person.name=='鈴木 千代').one_or_404()
        print(person)
    except NotFound as e:
        print(e)
    person = Person.query.where(Person.phone_number == '21-0757-5168').one_or_404()
    print(person)
    
    start_time = time.time()
    # Person.query.get_or_404(100) 0.0002
    db.session.execute(db.Select(Person).where(Person.id==100)).fetchone()
    end_time = time.time()
    
    print('Execution time: ', end_time - start_time)
