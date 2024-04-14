from models import app, db, User, Profile

with app.app_context():
    user = db.session.get(User, 1)
    print(user.profile.full_name)
    
    profile = db.session.get(Profile, 1)
    print(profile.user.email)
