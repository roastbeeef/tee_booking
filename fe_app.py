# THIS FILE IS THE FLASK APPLICATION

# package imports
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta
import requests

# internal imports
# from front_end.data import ACTORS
from tee_booking.src.funcs import (
    get_names, 
    get_id,
    parse_html, 
    get_available_tee_times
)

# globals
from tee_booking.src.vars import FULL_BOOKING_URL
# TEMPLATE_DIR = os.path.abspath('../../frontend/src')

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
# remember to parameterise this later
BOOKING_HORIZON = 2
# BOOKING_DATE = datetime.strftime(datetime.today()+timedelta(days=BOOKING_HORIZON), "%Y-%m-%d")
DATE_TODAY = datetime.strftime(datetime.today(), "%Y-%m-%d")
BOOKING_DATE = DATE_TODAY # placeholder
BOOKING_URL_WITH_DATE = f'{FULL_BOOKING_URL}{BOOKING_DATE}'


# grabbing the available tee times from the MSGC site
# DEFAULT_DATE_STR = datetime.today().date().strftime("%Y-%m-%d")
DEFAULT_DATE_STR = "2022-12-27"
DEFAULT_DATE = datetime.strptime(DEFAULT_DATE_STR, "%Y-%m-%d").date()


# Flask-Bootstrap requires this line
Bootstrap(app)

# with Flask-WTF, each web form is represented by a class
# "NameForm" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    booking_date = DateField('Date:', default=DEFAULT_DATE, validators=[DataRequired()])
    booking_time = SelectField('Time:', validators=[DataRequired()])
    # submit = SubmitField('Submit')

# all Flask routes below
@app.route('/', methods=['GET', 'POST'])
def index():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html

    soup = parse_html(f'{FULL_BOOKING_URL}{DEFAULT_DATE_STR}')
    available_tee_times = get_available_tee_times(soup)

    form = BookingForm()
    form.booking_time.choices = available_tee_times

    # once complete, this is superfluous, but required for testing
    if request.method == 'POST':
        # this should be returning data from the database - which is actually the mid sussex website
        return f'<h1>Booking date: {form.booking_date.data}. Booking time: {form.booking_time.data}'

    return render_template('index.html', form=form)


@app.route('/booking_time/<booking_date>')
def booking_time(booking_date):
    """
    this page works perfectly, no need to change it!
    """
    soup = parse_html(f'{FULL_BOOKING_URL}{booking_date}')
    booking_times = get_available_tee_times(soup)

    booking_times_array = []

    for id, booking_time in enumerate(booking_times):
        time_obj = {}
        time_obj['id'] = id
        time_obj['name'] = booking_time
        booking_times_array.append(time_obj)

    return jsonify({'booking_times': booking_times_array})

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)