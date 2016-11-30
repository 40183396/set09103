
from models import db
from models import User

# insert data
db.session.add(User("stev", "steven@mail.com", "cookies"))
#db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("soph", "sophie@mail.com", "biffy"))

# commit the changes
db.session.commit()
