from models import db, app, Employee, Company, Author

def add_records():
    company1 = Company(name="ABC株式会社")
    company2 = Company(name="XYZ株式会社")
    company3 = Company(name="PQR株式会社")
    company4 = Company(name="MNO株式会社")
    
    db.session.add_all([company1, company2, company3, company4])
    db.session.commit()
    
    employee1 = Employee(name="Employee 1", company=company1)
    employee2 = Employee(name="Employee 2", company=company1)
    employee3 = Employee(name="Employee 3", company=company2)
    employee4 = Employee(name="Employee 4", company=company2)
    employee5 = Employee(name="Employee 5", company=company2)
    employee6 = Employee(name="Employee 6", company_id=1000)
    
    db.session.add_all([employee1, employee2, employee3,
                        employee4, employee5, employee6])
    db.session.commit()
    
with app.app_context():
    # add_records()
    # INNER JOIN
    sql = db.Select(Company.name, Employee.name).join(
        Employee, Company.id==Employee.company_id
    ).order_by(Company.id)
    print(sql)
    print(db.session.execute(sql).all())
    
    # LEFT JOIN
    sql = db.Select(Company.name, Employee.name).join(
        Employee, Company.id==Employee.company_id, isouter=True
    ).order_by(Company.id)
    print(sql)
    print(db.session.execute(sql).all())
    
    # FULL OUTER JOIN
    sql = db.Select(Company.name, Employee.name).join(
        Employee, Company.id==Employee.company_id, full=True
    ).order_by(Company.id)
    print(sql)
    print(db.session.execute(sql).all())
    
    sql = db.Select(
        Company.name.label("company_name"), Employee.name.label("employee_name")
    ).join(
        Employee, Company.id==Employee.company_id
    ).filter(
        Company.name == "ABC株式会社"
    ).order_by(Company.id)
    
    for row in db.session.execute(sql).all():
        print(row.employee_name)
    
    sql = db.Select(Employee, Author).join(
        Author, Employee.id == Author.id
    )
    print(sql)
    print(db.session.execute(sql).all())
    for row in db.session.execute(sql).all():
        employee = row[0]
        author = row[1]
        print(employee.name, author.author_name)
    