"""Models for flask-notes app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """ Model representing the 'notes' table in the database. """

    __tablename__ = 'users'
    username = db.Column(db.String(20), primary_key = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)

    # flavor = db.Column(db.String, nullable = False)
    # size = db.Column(db.String, nullable = False)
    # rating = db.Column(db.Integer, nullable = False)
    # image = db.Column(db.String, nullable = False, default = 'https://tinyurl.com/demo-cupcake')

# class Note(db.Model):
#     """ Model representing the 'notes' table in the database. """

#     __tablename__ = 'notes'
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)