"""Models for flask-notes app."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """ Model representing the 'notes' table in the database. """

    __tablename__ = 'users'
    username = db.Column(db.String(20), primary_key = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """ Registers user with a hashed password, then returns the user. """
        print('User.register()')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username = username, password = hashed_password, email = email, first_name = first_name, last_name = last_name)

    @classmethod
    def authenticate(cls, username, password):
        """ Validate if given username exists and the password is correct. """
        print('User.authenticate()')
        user = User.query.filter_by(username = username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


    # flavor = db.Column(db.String, nullable = False)
    # size = db.Column(db.String, nullable = False)
    # rating = db.Column(db.Integer, nullable = False)
    # image = db.Column(db.String, nullable = False, default = 'https://tinyurl.com/demo-cupcake')

# class Note(db.Model):
#     """ Model representing the 'notes' table in the database. """

#     __tablename__ = 'notes'
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)