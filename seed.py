from models import User, db #TODO: import Note once written
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add users
user1 = User.register(username = 'wayne', password = '123456', email = "w@gmail.com", first_name = "Wayne", last_name = "Chen")
user2 = User.register(username = 'rain', password = '`12345', email = "r@gmail.com", first_name = "Rain", last_name = "Babauta")

# TODO: Add notes

# Finish transaction
db.session.add(user1)
db.session.add(user2)
db.session.commit()