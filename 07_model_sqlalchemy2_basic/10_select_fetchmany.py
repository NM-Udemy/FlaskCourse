from models import Person, db, app
from sqlalchemy.orm.exc import MultipleResultsFound

with app.app_context():
    result = db.session.execute(db.Select(Person).limit(50)) # ResultSet
    print('Many 1: ', result.fetchmany(1)) # 1行取得
    print('Many 10: ', result.fetchmany(10)) # 10行取得
    print('Many 20: ', result.fetchmany(20)) # 20行取得

    print('all: ', result.fetchall()) # 全取得 (allでも可)
    print('Many 1: ', result.fetchmany(1)) # []
    print('fetchone: ', result.fetchone()) # None
    
    result = db.session.execute(db.Select(Person).limit(50)) # ResultSet
    
    while rows := result.fetchmany(10):
        for row in rows:
            print(row[0])

