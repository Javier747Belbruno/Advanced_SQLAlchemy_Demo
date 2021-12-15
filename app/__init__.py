from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


from app import views
from app import models

db.create_all()
db.session.commit()
