# crud.py
from model import db, Person

db.create_all() # テーブルの作成

man1 = Person('Taro', 18)
man2 = Person('Jiro', 17)
man3 = Person('Saburo', 16)

print(man1, man2, man3)
db.session.add_all([man1, man2]) # 複数一緒に追加
db.session.add(man3) # 1つ追加

db.session.commit()
print(man1, man2, man3)