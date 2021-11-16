# crud.py

from model import db, Person
from datetime import datetime

man1 = Person(
    'Taro',
    '090-2222-2222',
    21,
    datetime.now(),
    datetime.now()
)
man2 = Person(
    'Jiro',
    '090-4444-4444',
    22,
    datetime.now(),
    datetime.now()
)
man3 = Person(
    'Saburo',
    '090-3333-3333',
    23,
    datetime.now(),
    datetime.now()
)
# db.session.add_all([man1, man2, man3])
# db.session.commit()

# print(Person.query.get(3)) # 主キーでの取り出し
# print(Person.query.first())
# for x in Person.query.filter_by(name='mike').all():
#     print(x.name)

# for x in Person.query.filter(Person.name.endswith('o')).limit(2).all():
#     print(x)


# データの削除
# id 1を削除
# Person.query.filter_by(id=1).delete()
# db.session.commit()

# データの更新

Person.query.filter_by(name='nanashi').update(
    {
        'name': 'John',
        'update_at': datetime.now()
    }
)
db.session.commit()
