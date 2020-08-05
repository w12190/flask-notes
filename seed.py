from models import User, db, Note
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add users
user1 = User.register(
  username = 'wayne',
  password = '123456',
  email = "w@gmail.com",
  first_name = "Wayne",
  last_name = "Chen",
)
user2 = User.register(
  username = 'rain',
  password = '`12345',
  email = "r@gmail.com",
  first_name = "Rain",
  last_name = "Babauta",
)

# Add notes
#title content owner
note1 = Note(title = 'The best note', content = 'This is good content', owner = user1.username)
note2 = Note(title = 'The okayest note', content = 'This is ok content', owner = user2.username)

# Finish transaction
db.session.add(user1)
db.session.add(user2)
db.session.add(note1)
db.session.add(note2)
db.session.commit()