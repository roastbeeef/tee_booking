# THIS FILE IS THE FLASK APPLICATION

# package imports
import json, uuid, requests, re, boto3
from flask import (
    Flask, 
    render_template, 
    redirect, 
    url_for, 
    request, 
    jsonify
    )
from flask_bootstrap import Bootstrap
from datetime import datetime
from urllib.request import urlopen
from boto3.dynamodb.conditions import Key, Attr
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager, 
    UserMixin, 
    login_user, 
    login_required, 
    logout_user, 
    current_user
    )


# internal imports
# from front_end.data import ACTORS
from tee_booking.src.funcs import (
    AdvanceTeeBooking
)
from tee_booking.src.forms import (
    BookingForm,
    LoginForm,
    RegistrationForm
)

from tee_booking.src.vars import (
    FULL_BOOKING_URL,
    DEFAULT_DATE_STR,
    DRIVER,
    LOGIN_PAYLOAD,
    url_base,
    TRANSACTIONS_TABLE_OBJECT,
    USERS_TABLE_OBJECT
    )

DRIVER.create_options

# this all needs to go somewhere else as well

from tee_booking.src.secrets import (
    aws_region,
    access_key,
    secret_access_key
)

dynamo_client = boto3.resource(
    service_name = 'dynamodb',
    region_name = aws_region,
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key
    )

app = Flask(__name__)
# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# TEMPLATE_DIR = os.path.abspath('../../frontend/src')

# remember to parameterise this later
BOOKING_HORIZON = 2
# BOOKING_DATE = datetime.strftime(datetime.today()+timedelta(days=BOOKING_HORIZON), "%Y-%m-%d")
DATE_TODAY = datetime.strftime(datetime.today(), "%Y-%m-%d")
BOOKING_DATE = DATE_TODAY # placeholder
BOOKING_URL_WITH_DATE = f'{FULL_BOOKING_URL}{BOOKING_DATE}'

# Flask-Bootstrap requires this line
Bootstrap(app)
atb = AdvanceTeeBooking(webdriver_loc=DRIVER, url=url_base)
# with Flask-WTF, each web form is represented by a class
# "NameForm" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
# all Flask routes below

@app.route('/', methods=['GET', 'POST'])
def landing_page():
    """
    placeholder for login system, currently redirects to booking form
    """
    return redirect(url_for('view_bookings'))

@app.route('/booking_form', methods=['GET', 'POST'])
def booking_form():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html    
    booking_url = f"{FULL_BOOKING_URL}+{DEFAULT_DATE_STR}"
    available_tee_times = atb.get_available_tee_times(booking_url, LOGIN_PAYLOAD)

    form = BookingForm()
    form.booking_time.choices = available_tee_times
    if request.method == 'POST':
        # is the booking date in the past? therefore, 
        url = f'{request.url_root}{"booking_time"}/{form.booking_date.data}'
        tee_times_response = urlopen(url)
        tee_times_data = json.loads(tee_times_response.read())
        tee_time_selection = tee_times_data["booking_times"][int(form.booking_time.data)]
        
        """
        TODO: this is the point in which the file gets written to dynamo
        TODO: before the below, add a nav bar, burger menu and "my bookings" page
        TODO: also create another route that has a jQuery table showing the contents
        """

        booking_payload = atb.create_tee_booking_transaction(
            username='test_123', 
            course_id='msgc', 
            booking_date=form.booking_date.data,
            booking_time=tee_time_selection["name"]
            )

        # move this once testing is complete
        
        atb.insert_data_into_dynamodb(TRANSACTIONS_TABLE_OBJECT, booking_payload)

        # inject this response into the HTML
        return f'<h1>Booking date: {form.booking_date.data}. Booking time: {tee_time_selection["name"]}'

    return render_template('index.html', form=form, user='Matt')



import sys
@app.route('/tee_bookings')
def view_bookings():
    # TODO: add filtering system to allow user to scan their bookings
    response = TRANSACTIONS_TABLE_OBJECT.scan(FilterExpression=Attr('username').eq('testing'))
    booking_data = json.dumps(response, cls=DecimalEncoder)
    return render_template('view_bookings.html', booking_data=booking_data, title='view bookings')


## APIs
@app.route('/booking_time/<booking_date>')
def booking_time(booking_date):
    """
    this page works perfectly, no need to change it!
    """

    # turn this into a function
    booking_url = f"{FULL_BOOKING_URL}+{booking_date}"
    available_tee_times = atb.get_available_tee_times(booking_url, LOGIN_PAYLOAD)

    booking_times_array = []
    for id, booking_time in enumerate(available_tee_times):
        time_obj = {}
        time_obj['id'] = id
        time_obj['name'] = booking_time
        booking_times_array.append(time_obj)

    return jsonify({f'booking_times': booking_times_array})








# CURRENTLY DESCOPED
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         # TODO: factor in the correct response here
#         user = User.get_user(form.username.data)
#         if user:
#             if check_password_hash(user.password, form.password.data):
#                 login_user(user, remember=form.remember_me.data)
#                 return redirect(url_for('booking_form'))
#         return '<h1>Invalid username or password</h1>'

#     return render_template('login.html', form=form)

# CURRENTLY DESCOPED
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # TODO: when a user is created, make sure that user isnt already in the database
#     # TODO: this needs to be for email AND username (i.e. this username is already registered)
#     # TODO: implement email verification with an account active flag
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         hashed_password = generate_password_hash(form.password.data, method='sha256')
#         new_user = User(
#             id=uuid.uuid4(),
#             username=form.username.data,
#             password=hashed_password,
#             email_address=form.email_address.data
#         )
#         USERS_TABLE_OBJECT.put_item(Item=new_user.dict())

#         return f'<h1> New user has been created! </h1>'

#     return render_template('register.html', form=form)

# from dataclasses import dataclass, asdict

# @dataclass
# class User(UserMixin):
#     # TODO: this class needs to be moved somewhere else
#     def __init__(self, id, username, email_address, password) -> None:
#         self.id = id
#         self.username = username
#         self.email_address = email_address
#         self.password = password

#     id: str
#     username: str
#     email_address: str
#     password: str

#     def dict(self):
#         return {k: str(v) for k, v in asdict(self).items()}

#     @staticmethod
#     def get_user(username):
#         response = USERS_TABLE_OBJECT.query(
#             KeyConditionExpression=Key('username').eq(username)
#             )
#         if response['Count'] == 0:
#             return
#         user = User(
#             id=response['Items'][0]['id'],
#             username=response['Items'][0]['username'], 
#             email_address=response['Items'][0]['email_address'], 
#             password=response['Items'][0]['password']
#         )
#         return user

# # @login_manager.user_loader
# def load_user(user_id):
#     # TODO: this wont work - adjust to work with dynamoDB.
#     return User.get_user(user_id)

if __name__ == '__main__':
    app.run(debug=True)