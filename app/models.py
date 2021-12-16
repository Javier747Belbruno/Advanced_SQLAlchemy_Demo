from app import db


class UserSubreddit(db.Model):
    __tablename__ = "user_subreddit_role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    subreddit_id = db.Column(db.Integer, db.ForeignKey("subreddit.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)

    __table_args__ = (db.UniqueConstraint(user_id, subreddit_id, role_id),)

    user = db.relationship("User", back_populates="user_subreddit_role")
    subreddit = db.relationship("Subreddit")
    role = db.relationship("Role", back_populates="user_subreddit_role")

    def __str__(self):
        return "UserSubreddit(user_id={}, subreddit_id={}, role_id={})".format(self.user_id, self.subreddit_id, self.role_id)

class RolePermission(db.Model):
    __tablename__ = "role_permission"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey("permission.id"), nullable=False)

    __table_args__ = (db.UniqueConstraint(role_id, permission_id),)

    role = db.relationship("Role", back_populates="role_permission")
    permission = db.relationship("Permission", back_populates="role_permission")

    def __str__(self):
        return "RolePermission(role_id={}, permission_id={})".format(self.role_id, self.permission_id)

class Permission(db.Model):
    __tablename__ = "permission"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

    role_permission = db.relationship("RolePermission", back_populates="permission")

    def __str__(self):
        return "Permission(name={})".format(self.name)

class Subreddit(db.Model):
    __tablename__ = 'subreddit'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True)

    def __str__(self):
        return "Subreddit(name={})".format(self.name)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60), index=True, unique=True)
    user_subreddit_role = db.relationship("UserSubreddit", back_populates="user")

    def __str__(self):
        return "User(username={})".format(self.username)

class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True)
    user_subreddit_role = db.relationship("UserSubreddit", back_populates="role")
    role_permission = db.relationship("RolePermission", back_populates="role")

    def __str__(self):
        return "Role(name={})".format(self.name)