"""Flask app for Notes"""
from flask import Flask, request, jsonify
from models import db, connect_db, Note #TODO import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def show_homepage():
    """ Redirects user to '/register' """
    print('show_homepage()')
    return redirect('/register')

@app.route('/register', methods = ['GET', 'POST'])
def registration_form():
    """ Shows a registration form if GET; handles the registration form if POST. """
    print('registration_form()')

    # TODO: WTForm for the registration stuff
    return render_template('registration_form.html')


@app.route('/login', methods = ['GET', 'POST'])
def login_form():
    """ Shows login form if GET; handles login form if POST.  """
    print('login_form()')

    return render_template('login_form.html')

@app.route('/secret')
def show_secret():
    """ Shows the secret page. """
    print('show_secret()')

    return "You made it!"