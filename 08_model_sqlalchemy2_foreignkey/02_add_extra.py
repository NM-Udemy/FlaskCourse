from models import app, db, Company, Employee

with app.app_context():
    company = db.session.get(Company, 1)
    employee = Employee(name="石井士郎", company_id=company.id)
    # db.session.add(employee)
    # db.session.commit()
    
    sql = db.Select(Company).where(Company.name=="株式会社ABC")
    company = db.session.execute(sql).one_or_none()
    if company:
        employee = Employee(name="吉田美子", company=company[0])
        db.session.add(employee)
        db.session.commit()