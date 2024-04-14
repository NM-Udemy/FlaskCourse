from models import Person, db, app
import time

with app.app_context():
    sql = db.Select(Person)
    overall_start_time = time.time()
    start_time = time.time()
    for row in db.session.execute(sql).yield_per(100):
        print("execution_time: ", start_time - time.time())
        print(row)
        start_time = time.time()
    
    overall_end_time = time.time()
    print('Overall Time: ', overall_end_time - overall_start_time) # 0.00967097282409668

    sql = db.Select(Person)
    overall_start_time = time.time()
    start_time = time.time()
    for row in db.session.execute(sql, execution_options={"yield_per": 100}).fetchone():
        print("execution_time: ", start_time - time.time())
        print(row)
        start_time = time.time()
    
    overall_end_time = time.time()
    print('Overall Time: ', overall_end_time - overall_start_time) # 0.00967097282409668
