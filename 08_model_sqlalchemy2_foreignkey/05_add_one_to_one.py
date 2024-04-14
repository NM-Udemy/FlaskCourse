from models import app, db, User, Profile

with app.app_context():
    # user = User(username="johndoe", email="johndoe@mail.com")
    # profile = Profile(full_name="John Doe", location="New York", user=user)
    # db.session.add_all([user, profile])
    # db.session.commit()
    profile = Profile(full_name="John Doe", location="Tokyo", user_id=1)
    db.session.add(profile)
    db.session.commit()
    