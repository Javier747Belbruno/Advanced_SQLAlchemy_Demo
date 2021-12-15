from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.String(100), nullable= True)
    user_password = db.Column(db.String(150), nullable = True)
    user_phone = db.Column(db.String(20), nullable = True)