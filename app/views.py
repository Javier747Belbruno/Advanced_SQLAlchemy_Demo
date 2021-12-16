import sqlalchemy
from app import app, db
from app.models import Permission, User, UserSubreddit, Role, Subreddit, RolePermission, Permission




@app.route("/")
def index():
    return "Root page of the application"


#add route for /users/<username>
@app.route("/users/<username>")
def add(username):
    user = User(username = username)
    db.session.add(user)
    db.session.commit()
    return "User added"

#return all users
@app.route("/users")
def get_users():
    users = User.query.all()
    users_list = [user.__str__() for user in users]
    return str(users_list)

#return all subreddits
@app.route("/subreddits")
def get_subreddits():
    subreddits = Subreddit.query.all()
    subreddits_list = [subreddit.__str__() for subreddit in subreddits]
    return str(subreddits_list)

#return all subreddits for a user
@app.route("/users/<username>/subreddits")
def get_user_subreddits(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return "User not found"
    user_subreddits = UserSubreddit.query.filter_by(user_id=user.id).all()
    #return subreddits name
    user_subreddits_list = [user_subreddit.subreddit.name for user_subreddit in user_subreddits]
    return str(user_subreddits_list)

#add a subreddit to a user
@app.route("/users/<username>/subreddits/<subreddit_name>")
def add_user_subreddit(username, subreddit_name):
    user = User.query.filter_by(username=username).first()
    subreddit = Subreddit.query.filter_by(name=subreddit_name).first()
    user_subreddit = UserSubreddit(user=user, subreddit=subreddit, role=Role.query.filter_by(name="user").first())
    db.session.add(user_subreddit)
    db.session.commit()
    return "UserSubreddit added"


@app.route("/addToDB")
def add_to_db():
    #Insert data into the database
    try:    
        user = User(username = "u1")
        subreddit = Subreddit(name = "s1")
        role = Role(name = "r1")
        db.session.add(user)
        db.session.add(subreddit)
        db.session.add(role)
        user = User(username = "u2")
        db.session.add(user)
        subreddit = db.session.query(Subreddit).filter(Subreddit.name == "s1").first()
        user = db.session.query(User).filter(User.username == "u1").first()
        role = db.session.query(Role).filter(Role.name == "r1").first()
        assoc = UserSubreddit(user=user, subreddit=subreddit, role=role)
        db.session.add(assoc)
        permission = Permission(name = "p1")
        db.session.add(permission)
        role_permission = RolePermission(role=role, permission=permission)
        db.session.add(role_permission)
        db.session.commit()
        return "Data added to database"
    except Exception as e:
        return str(e)

#insert a RolePermission
@app.route("/RolePermission/<role_name>/<permission_name>")
def add_role_permission(role_name, permission_name):
    try:
        role = Role.query.filter_by(name=role_name).first()
        permission = Permission.query.filter_by(name=permission_name).first()
        if role is None:
            return "Role not found"
        if permission is None:
            return "Permission not found"
        role_permission = RolePermission(role=role, permission=permission)
        db.session.add(role_permission)
        db.session.commit()
        return "RolePermission added"
    #sqlAlchemy exception
    except sqlalchemy.exc.IntegrityError as e:
        return "RolePermission already exists"
    except Exception as e:
        return str(e)


#insert a subreddit
@app.route("/subreddits/<subreddit_name>")
def add_subreddit(subreddit_name):
    subreddit = Subreddit(name = subreddit_name)
    db.session.add(subreddit)
    db.session.commit()
    return "Subreddit added"

#insert a user
@app.route("/users/<username>")
def add_user(username):
    user = User(username = username)
    db.session.add(user)
    db.session.commit()
    return "User added"

#insert a role
@app.route("/roles/<name>")
def add_role(name):
    role = Role(name = name)
    db.session.add(role)
    db.session.commit()
    return "Role added"

#insert a role for a user and a subreddit
@app.route("/users/<username>/subreddits/<subreddit_name>/roles/<name>")
def add_user_subreddit_role(username, subreddit_name, name):
    user = User.query.filter_by(username=username).first()
    subreddit = Subreddit.query.filter_by(name=subreddit_name).first()
    role = Role.query.filter_by(name=name).first()
    user_subreddit = UserSubreddit(user=user, subreddit=subreddit, role=role)
    db.session.add(user_subreddit)
    db.session.commit()
    return "UserSubreddit added"

#get role for a user and a subreddit
@app.route("/users/<username>/subreddits/<subreddit_name>/roles")
def get_user_subreddit_role(username, subreddit_name):
    user = User.query.filter_by(username=username).first()
    subreddit = Subreddit.query.filter_by(name=subreddit_name).first()
    print(user.username + " " + subreddit.name)
    user_subreddit = UserSubreddit.query.filter_by(user=user, subreddit=subreddit).first()
    return user_subreddit.role.name