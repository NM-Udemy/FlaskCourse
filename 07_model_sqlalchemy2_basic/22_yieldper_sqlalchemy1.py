from models_sqlalchemy1 import Person, db, app
import time

with app.app_context():
    query = Person.query
    overall_start_time = time.time()
    start_time = time.time()
    for index, row in enumerate(query.yield_per(100)):
        print(f"{index} execution_time: {start_time - time.time()}")
        start_time = time.time()
    overall_end_time = time.time()
    print(f"Overall time: {overall_end_time - overall_start_time}")
