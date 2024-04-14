from models import Person, db, app
from sqlalchemy.orm.exc import MultipleResultsFound

with app.app_context():
    result = db.session.execute(db.Select(Person))
    try:
        print(result.one()) # MultipleResultsFound, 1行はOK。それ以外はエラー
    except MultipleResultsFound as e:
        print(e)
    sql = db.Select(Person).limit(1)
    print(sql)
    result = db.session.execute(sql)
    print(result.one()[0])
    # print(result.one()[0]) # 1行取得したらclose
    
    sql = db.Select(Person).limit(0)
    result = db.session.execute(sql)
    print(result.one_or_none()) # 1つかNone, 2行以上はエラー
    
    person = db.session.get(Person, 10001) # SQLの実行からデータの取得(主キーを指定)
    print(person)
