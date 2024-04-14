from models import app, db, Company, Employee

with app.app_context():
    company = db.session.get(Company, 1)
    # Company.query.get(1)
    print(company)
    print(company.employees)
    
    # Employee側
    employee = db.session.get(Employee, 1)
    print(employee.company)
    print(employee.company.name)
    
    