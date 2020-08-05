from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField#SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, length
import email_validator


class RegistrationForm(FlaskForm):
    """Form for registering a user."""
    username = StringField("Username: ", validators=[InputRequired(), length(min = 3, max = 20)])
    password = PasswordField("Password: ", validators = [length(min = 6)])
    email = StringField("Email: ", validators = [length(min = 7, max = 50), Email()])
    first_name = StringField("First Name: ", validators = [length(max = 30)])
    last_name = StringField("Last Name: ", validators = [length(max = 30)])

class LoginForm(FlaskForm):
    """ Form for logging in a user. """
    username = StringField("Username: ", validators=[InputRequired(), length(min = 3, max = 20)])
    password = PasswordField("Password: ", validators = [length(min = 6)])

class NoteForm(FlaskForm):
    """ Form for making a new note """
    title = StringField("Title: ", validators=[InputRequired(), length(max = 100)])
    content = StringField("Content: ", validators=[InputRequired()])

class EditNoteForm(FlaskForm):
    """ Form for editing a note """
    title = StringField("Title: ", validators=[InputRequired(), length(max = 100)])
    content = StringField("Content: ", validators=[InputRequired()])