""" this file contains all of the constants """
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tee_booking.src.credentials import USERNAME, PASSWORD

# chromedriver location
chrome_options = Options()
chrome_options.headless = True
DRIVER = webdriver.Chrome(executable_path = r'../resources/chromedriver', options=chrome_options)


url_base = "http://www.midsussexgolfclub.co.uk/"
url_booking_ext = "memberbooking/?date="
url_authentication_ext = "login.php"
msgc_suffix = '&course=41&group=1'

FULL_BOOKING_URL = url_base + url_booking_ext
FULL_AUTH_URL = url_base + url_authentication_ext

# DEFAULT_DATE_STR = datetime.today().date().strftime("%Y-%m-%d")
DEFAULT_DATE_STR = "2023-01-13"
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