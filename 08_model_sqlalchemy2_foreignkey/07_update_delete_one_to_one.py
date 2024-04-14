from models import app, db, User, Profile

with app.app_context():
    user = db.session.get(User, 1)
    user.profile.location = "Tokyo"
    db.session.commit()
    
    db.session.delete(user.profile)
    db.session.commit()
    