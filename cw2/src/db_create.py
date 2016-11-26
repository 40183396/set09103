from app import db
from models import WallPosts

#create database and tables
db.create_all()

#insert
db.session.add(WallPosts("Good", "I am feeling pretty good"))
db.session.add(WallPosts("Hello", "Hello from the other side"))

#commit
db.session.commit()

