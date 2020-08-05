"""Flask app for Notes"""
from flask import Flask, request, jsonify, redirect, render_template, session, flash
from models import db, connect_db, User, Note
from forms import RegistrationForm, LoginForm, NoteForm, EditNoteForm
from flask_bcrypt import Bcrypt

SECRET_KEY = "secret global key lol"

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_notes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rainb:qwerty@localhost/flask_notes'
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

        new_user = User.register(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name,
        )

        #Complete transaction
        db.session.add(new_user)
        db.session.commit()

        #can add a login after register
        current_user = User.authenticate(username = username, password = password)
        if current_user != False:
            session["user_username"] = current_user.username
            return redirect(f'/users/{username}')
        else:
            login_form.username.errors = ["Incorrect name or password, please try again."]

        return redirect(f'/users/{username}')
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
            session["user_username"] = current_user.username
            return redirect(f'/users/{username}')
        else:
            login_form.username.errors = ["Incorrect name or password, please try again."]
    
    return render_template('login_form.html', form = login_form)

@app.route('/logout')
def logout():
    """Logs user out and redirects to homepage."""
    print('logout()')

    if session.get("user_username"):
        session.pop("user_username")

    return redirect('/')

@app.route('/users/<username>')
def show_user_detail(username):
    """ Shows the user_detail page. """
    print('show_user_detail()')

    if "user_username" not in session:
        flash("You must be logged in!")
        return redirect("/login")
    else:
        user = User.query.get_or_404(username)
        notes = user.notes
        return render_template("user_detail.html", user = user, notes = notes)

@app.route('/users/<username>/delete', methods=['POST'])
def delete_user(username):
    """Remove the user from the database and make sure to also delete all of their notes.
    Clear any user information in the session and redirect to /."""
    print("delete_user()")

    user = User.query.get_or_404(username)

    db.session.delete(user)
    db.session.commit()
    return redirect('/')

@app.route('/users/<username>/notes/add', methods=['GET', 'POST'])
def add_note(username):
    """Display a form to add notes.
    Add a new note and redirect to /users/<username>"""
    print("add_note()")

    user = User.query.get_or_404(username)

    note_form = NoteForm()

    if note_form.validate_on_submit():
        title = note_form.title.data
        content = note_form.content.data

        new_note = Note(title=title, content=content, owner=user.username)

        db.session.add(new_note)
        db.session.commit()

        return redirect(f'/users/{username}')
    else:
        return render_template('note_form.html', form=note_form)

@app.route('/notes/<int:id>/update', methods=['GET', 'POST'])
def edit_note(id):
    """Display a form to edit a note.
    Update a note and redirect to* /users/<username>*."""
    print("edit_note()")
    note = Note.query.get_or_404(id)

    edit_note_form = EditNoteForm(obj=note)

    if edit_note_form.validate_on_submit():
        note.title = edit_note_form.title.data
        note.content = edit_note_form.content.data

        db.session.commit()

        return redirect(f'/users/{note.owner}')
    else:
        return render_template('edit_note_form.html', form=edit_note_form, note=note)

@app.route('/notes/<int:id>/delete', methods=['POST'])
def delete_note(id):
    """Delete a note and redirect to /users/<username>."""
    print("delete_note()")

    note = Note.query.get_or_404(id)

    db.session.delete(note)
    db.session.commit()

    return redirect(f'/users/{note.owner}')