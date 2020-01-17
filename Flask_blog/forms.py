from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class RegistrationForm(FlaskForm):
    username = StringField("Username")

    email = StringField("Email")

    password = PasswordField("Password")

    confirm_password = PasswordField("Confirm Password")

    submit = SubmitField("Sign Up")



class LoginForm(FlaskForm):
    
    email = StringField("Email")

    password = PasswordField("Password")

    remember = BooleanField("Remember me")

    submit = SubmitField("Log in")