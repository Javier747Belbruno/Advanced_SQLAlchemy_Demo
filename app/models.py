from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)

class Subreddit(db.Model):
    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)  

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)    

class SubredditXUserXRole(db.Model):
    #id  column autoincrement
    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    subreddit_id = db.Column(db.Integer, db.ForeignKey('subreddit.id'), nullable = False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable = False)

class RoleXPermission(db.Model):
    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable = False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), nullable = False)

