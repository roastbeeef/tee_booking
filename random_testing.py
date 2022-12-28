import boto3

from src.secrets import (
    aws_region,
    access_key,
    secret_access_key
)

TRANSACTIONS_TABLES_NAME = "teebooking-transactions"


dynamo_client  =  boto3.resource(
    service_name = 'dynamodb',
    region_name = aws_region,
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key
    )

dynamo_client.get_available_subresources()

transactions_table = dynamo_client.Table(TRANSACTIONS_TABLES_NAME)
transactions_table.table_status


""" these assets will be used to book the tee time """
from datetime import datetime
import re

def create_transaction_id(timestamp, username, booking_date, booking_time):
    """function to create an almost-unique transaction ID"""
    return f"{timestamp}{username.upper()}{booking_date}{booking_time}"

def strip_non_alphanumeric(input_string) -> str:
    """function to strip non alphanumeric from a string"""
    return re.sub(r'[^\w\s]', '', input_string)

test_username = "testing"
test_course_id = "0001"
test_booking_date = "2023-01-01"
test_booking_time = "07:00"

def create_transaction(
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


transactions_table.put_item(
    Item = create_transaction(test_username, test_course_id, test_booking_date, test_booking_time)
        )


