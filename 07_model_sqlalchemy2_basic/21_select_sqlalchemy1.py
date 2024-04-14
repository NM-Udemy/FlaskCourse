from models_sqlalchemy1 import Person, db, app
from sqlalchemy import and_, or_, func

def print_under():
    print('-' * 100)

with app.app_context():
    query = Person.query
    print(query) # SQL
    print(query.first()) # id=1, name=佐々木 加奈, age=27
    print(query.first()) # id=1, name=佐々木 加奈, age=27
    print_under()
    print(Person.query.order_by(Person.age.desc()).first())
    
    results = Person.query.filter(Person.age==20).all()
    for r in results:
        print(type(r), r)
    
    # one
    print_under()
    print(Person.query.limit(1).one())
    
    # カラム絞り込み
    for result in Person.query.with_entities(Person.age.label('年齢'), Person.name).filter(Person.age>75).all():
        print(result.年齢)
    print(Person.query.with_entities(Person.age.label('年齢'), Person.name).filter(Person.age>75))
    
    print_under()
    print(Person.query.with_entities(Person.id, Person.name).filter(
        Person.name.startswith('山口')).order_by(Person.id.desc()).all()
    )
    
    print(Person.query.filter(and_(
        Person.name.startswith('山口'), Person.age>50
    )).all())
    
    print(Person.query.with_entities(Person.age, Person.name).filter(or_(
        Person.age<25, Person.age>75
    )).all())
    
    print_under()
    print(Person.query.filter(Person.name.like('%田%')).with_entities(
        Person.age, Person.name
    ).all())
    
    print(Person.query.filter(Person.id.in_([1,2,3])).all())
    
    # function, group by
    print_under()
    print(Person.query.with_entities(
        func.count(Person.id), func.sum(Person.age), func.max(Person.age)).all()
    )
    
    sql = Person.query.with_entities(
        Person.age, func.count(Person.id).label('id_count'),
        func.max(Person.id).label('id_max')
    ).filter(Person.id>=500).group_by(
        Person.age
    ).order_by(func.count(Person.id).desc())
    print(sql)
    
    for row in sql.all():
        print(row.age, row.id_count, row.id_max)
