from app import app, db
from app.models import User, Subreddit, Role, Permission, SubredditXUserXRole, RoleXPermission



@app.route("/")
def index():
    return "Hello world"

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
    user_list = ""
    for user in users:
        #if user.user_phone is None continue
        user_list += "<br>" + user.username + " phone_number> "
        if user.user_phone is not None:
            user_list += user.user_phone + ","
        else:
            user_list += "No phone number"
    return user_list

#change phone number for a user
@app.route("/users/<username>/<phone_number>")
def change_phone(username, phone_number):
    try:
        user = User.query.filter_by(username = username).first()
        user.user_phone = phone_number
        db.session.commit()
        return "Phone number changed"
    except Exception as e:
        return "User not found" + str(e)


@app.route("/addToDB")
def add_to_db():
    #Insert data into the database
    db.session.add(User(username = 'Javier'))
    db.session.add(User(username = 'Mike'))
    db.session.add(Subreddit(name = 'Promiedos'))
    db.session.add(Subreddit(name = 'Fulbo'))
    db.session.add(Role(name = 'admin'))
    db.session.add(Role(name = 'user'))
    db.session.add(Permission(name = 'create_post'))
    db.session.add(Permission(name = 'edit_post'))
    db.session.add(Permission(name = 'delete_post'))
    db.session.add(SubredditXUserXRole(user_id = 1, subreddit_id = 1, role_id = 1))
    db.session.add(SubredditXUserXRole(user_id = 2, subreddit_id = 2, role_id = 2))
    db.session.add(RoleXPermission(role_id = 1, permission_id = 1))
    db.session.add(RoleXPermission(role_id = 1, permission_id = 2))
    db.session.add(RoleXPermission(role_id = 1, permission_id = 3))
    db.session.add(RoleXPermission(role_id = 2, permission_id = 1))

    db.session.commit()
    return "Added to DB"





