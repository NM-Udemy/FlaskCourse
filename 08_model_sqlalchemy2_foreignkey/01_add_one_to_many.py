from models import app, db, Company, Employee

with app.app_context():
    company1 = Company(name="株式会社ABC")
    company2 = Company(name="株式会社XYZ")
    
    employee1 = Employee(name="山田太郎", company=company1)
    employee2 = Employee(name="鈴木花子", company=company1)
    employee3 = Employee(name="佐藤次郎", company=company2)
    
    # セッションに追加
    db.session.add_all([company1, company2, employee1, employee2, employee3])
    db.session.commit()
