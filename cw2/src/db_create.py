from app import db
from models import WallPost

#create the database and dbtables
db.create_all()

# insert
db.session.add(WallPost("Good", "I am pretty darn good"))
db.session.add(WallPost("Well", "I\'m pretty well actually"))

# commit
db.session.commit()
