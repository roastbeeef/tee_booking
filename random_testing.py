import boto3
from datetime import datetime
import re

from tee_booking.src.secrets import (
    aws_region,
    access_key,
    secret_access_key
)

TRANSACTIONS_TABLES_NAME = "teebooking-transactions"
USERS_TABLE_NAME = "teebooking-users"

dynamo_client = boto3.resource(
    service_name = 'dynamodb',
    region_name = aws_region,
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key
    )

TRANSACTIONS_TABLE_OBJECT = dynamo_client.Table(TRANSACTIONS_TABLES_NAME)
USERS_TABLE_OBJECT = dynamo_client.Table(USERS_TABLE_NAME)


""" testing below """

test_username = "testing"
test_course_id = "0001"
test_booking_date = "2023-01-01"
test_booking_time = "07:00"


""" these assets will be used to book the tee time """


def create_transaction_id(timestamp, username, booking_date, booking_time):
    """function to create an almost-unique transaction ID"""
    return f"{timestamp}{username.upper()}{booking_date}{booking_time}"

def strip_non_alphanumeric(input_string) -> str:
    """function to strip non alphanumeric from a string"""
    return re.sub(r'[^\w\s]', '', input_string)

def create_tee_booking_transaction(
    username: str,
    course_id: str, 
    booking_date: int,
    booking_time: str,
    ) -> dict:
    """function to create a transaction payload"""
    timestamp = datetime.strftime(datetime.today(), format="%Y%m%d%H%M%S")
    return {
        'transaction_id': create_transaction_id(timestamp, username, booking_date, booking_time),
        'username': username,
        "course_id": str(course_id),
        "booking_date": int(strip_non_alphanumeric(booking_date)), # this will be converted to a date using the datetime package later
        "booking_time": str(strip_non_alphanumeric(booking_time)) # this can just be 4 digits and can be split later to give the colon in the middle
        }

TRANSACTIONS_TABLE_OBJECT.put_item(
    Item = create_tee_booking_transaction(test_username, test_course_id, test_booking_date, test_booking_time)
        )
        


from tee_booking.src.funcs import AdvanceTeeBooking
from tee_booking.src.vars import DRIVER, url_base, FULL_BOOKING_URL 
from flask import jsonify


atb = AdvanceTeeBooking(webdriver_loc=DRIVER, url=url_base)

booking_date = '13-01-2023'
soup = atb._get_html_document_and_parse(f'{FULL_BOOKING_URL}{booking_date}')
booking_times = atb.get_available_tee_times(soup)



booking_times_array = []

for id, booking_time in enumerate(booking_times):
    time_obj = {}
    time_obj['id'] = id
    time_obj['name'] = booking_time
    booking_times_array.append(time_obj)

booking_times_array

jsonify({'booking_times': booking_times_array})