from models import Person, db, app

with app.app_context():
    print(db.Select(Person)) # SELECT文
    print(type(db.Select(Person))) # sqlalchemy.sql.selectable.Select
    
    result = db.session.execute(db.Select(Person)) # DB上でSQL実行
    
    print(result.fetchone()[0]) # id: 1
    print(result.fetchone()[0]) # id: 2
    print(result.fetchone()[0]) # id: 3
    
    # 残りを取得して表示する
    while(row := result.fetchone()): # Noneになるまで実行
        print(row[0])
    
    print(result.fetchone())
    result = db.session.execute(db.Select(Person)) # DB上でSQL実行
    print(result.first()[0]) # 1つだけ取得。（DBとのコネクションをクローズ）
    print(result.first()[0])
    