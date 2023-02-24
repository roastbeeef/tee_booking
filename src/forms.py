""" this file contains the classes for all of the forms """
from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    SubmitField, 
    SelectField, 
    DateField, 
    PasswordField, 
    BooleanField
    )
from wtforms.validators import (
    DataRequired,
    InputRequired,
    Email,
    Length
)
from tee_booking.src.vars import DEFAULT_DATE

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    booking_date = DateField('Date:', default=DEFAULT_DATE, validators=[DataRequired()])
    booking_time = SelectField('Time:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember_me = BooleanField('Remember me')

class RegistrationForm(FlaskForm):
    email_address = StringField('email', validators=[InputRequired(), Email(message='Invalid Email Address'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
