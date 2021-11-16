from model import db, Employee, Project, Company

# create Employee
john = Employee('John')
adam = Employee('Adam')

# add employees
db.session.add_all([john, adam])
db.session.commit()

# create Compamy
company1 = Company('Microsoft', john.id)
company2 = Company('Apple', adam.id)

# add company
db.session.add_all([company1, company2])
db.session.commit()

# create projects
john_project1 = Project('Word Project', john.id)
john_project2 = Project('Excel Project', john.id)
adam_project1 = Project('Mac Project', adam.id)
adam_project2 = Project('Iphone Project', adam.id)

db.session.add_all(
    [john_project1, john_project2, adam_project1, adam_project2]
)

db.session.commit()