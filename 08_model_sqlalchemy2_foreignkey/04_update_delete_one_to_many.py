from models import app, db, Company, Employee

with app.app_context():
    company = db.session.get(Company, 1)
    for employee in company.employees:
        print(employee.name)
    
    company.employees[0].name = "山本太郎"
    db.session.commit()
    
    # db.session.delete(company.employees[3])
    # db.session.commit()