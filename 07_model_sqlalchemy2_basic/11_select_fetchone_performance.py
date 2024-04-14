from models import Person, db, app
import time

with app.app_context():
    result = db.session.execute(db.Select(Person)) # ResultSet
    start_time = time.time()
    row = result.fetchone() # 0.003368854522705078
    end_time = time.time()
    print('Time: ', end_time - start_time)
    
    start_time = time.time()
    row = result.fetchone() # 0.000030994415283203125e
    end_time = time.time()
    print('Time: ', end_time - start_time)
    
    print('-'*100)
    
    result = db.session.execute(db.Select(Person), execution_options={"yield_per": 10}) # ResultSet
    # result = db.session.execute(db.Select(Person), execution_options={"stream_results": True}) # サーバーサイドカーソル
    start_time = time.time()
    row = result.fetchone() # 4.506111145019531e-05
    end_time = time.time()
    print('Time: ', end_time - start_time)
    
    start_time = time.time()
    row = result.fetchone() # 9.5367431640625e-07
    end_time = time.time()
    print('Time: ', end_time - start_time)

    print(result.fetchall()) # 残り