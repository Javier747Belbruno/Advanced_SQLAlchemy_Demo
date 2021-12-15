from app import app, db
from app.models import User



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


