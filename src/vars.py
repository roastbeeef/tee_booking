""" this file contains all of the constants """
import boto3
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tee_booking.src.credentials import USERNAME, PASSWORD

# chromedriver location
chrome_options = Options()
chrome_options.headless = True
DRIVER = webdriver.Chrome(executable_path = r'../resources/chromedriver', options=chrome_options)


url_base = "https://www.midsussexgolfclub.co.uk/"
url_booking_ext = "memberbooking/?date="
url_authentication_ext = "login.php"
msgc_suffix = '&course=41&group=1'

FULL_BOOKING_URL = url_base + url_booking_ext
FULL_AUTH_URL = url_base + url_authentication_ext
FULL_LOGIN_URL = url_base + url_authentication_ext

# DEFAULT_DATE_STR = datetime.today().date().strftime("%Y-%m-%d")
DEFAULT_DATE_STR = "2023-01-26"
DEFAULT_DATE = datetime.strptime(DEFAULT_DATE_STR, "%Y-%m-%d").date()

# authentication
LOGIN_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
    'origin': url_base, 
    'referer': url_base + url_authentication_ext
    }

LOGIN_PAYLOAD = {
        'memberid': USERNAME,
        'pin': PASSWORD
        }

### db vars
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