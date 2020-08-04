"""Flask app for Notes"""
from flask import Flask, request, jsonify, redirect, render_template, session
from models import db, connect_db, User #TODO import Note
from forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt

SECRET_KEY = "secret global key lol"

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def show_homepage():
    """ Redirects user to '/register' """
    print('show_homepage()')
    return redirect('/register')

# username password email first_name last_name

@app.route('/register', methods = ['GET', 'POST'])
def registration_form():
    """ Shows a registration form if GET; handles the registration form if POST. """
    print('registration_form()')
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        #Pull data from form and create new User()
        username = registration_form.username.data
        password = registration_form.password.data
        email = registration_form.email.data
        first_name = registration_form.first_name.data
        last_name = registration_form.last_name.data

        new_user = User.register(username = username, password = password, email = email, first_name = first_name, last_name = last_name)

        #Complete transaction
        db.session.add(new_user)
        db.session.commit()

        return redirect('/secret')
    else:
        return render_template('registration_form.html', form = registration_form)


@app.route('/login', methods = ['GET', 'POST'])
def login_form():
    """ Shows login form if GET; handles login form if POST.  """
    print('login_form()')

    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        current_user = User.authenticate(username = username, password = password)

        if current_user != False:
            session[current_user.username] = current_user.username
            return redirect('/secret')
        else:
            login_form.username.errors = ["Incorrect name or password, please try again."]
    
    #TODO: add back else: and add copy of this return to inner if loop's else statement if there turns out to be bugs
    return render_template('login_form.html', form = login_form)

@app.route('/secret')
def show_secret():
    """ Shows the secret page. """
    print('show_secret()')

    return "You made it!"