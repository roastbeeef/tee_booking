# insertion works!

# from tee_booking.src.vars import (
#     TRANSACTIONS_TABLE_OBJECT
#     )
# import json


# table_data = TRANSACTIONS_TABLE_OBJECT.scan()

# len(table_data['Items'])

# this weekend! 
# 1) nav bar
# https://dev.to/brunooliveira/flask-series-part-9-adding-a-navbar-by-using-template-inheritance-2e5o
# https://arshovon.com/snippets/flask-bootstrap-navbar/
# https://www.techwithtim.net/tutorials/flask/adding-bootstrap/
# 2) jquery table
# https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
# 3) lambda function to book
# 4) scheduling
# 5) authentication - just really basic for now until hosted



# hosting - fully serverless!
# website on elastic beanstalk
# database on dynamodb
# scheduling on stepfunctions
# booking on lambda


# this works but returns nothing
from src.vars import FULL_BOOKING_URL, url_base, DRIVER, LOGIN_PAYLOAD
# from src.funcs import AdvanceTeeBooking
booking_url = f"{FULL_BOOKING_URL}27-02-2022"

# atb = AdvanceTeeBooking(webdriver_loc=DRIVER, url=url_base)

# tee_times = atb.get_available_tee_times(booking_url, LOGIN_PAYLOAD)
# print(tee_times)



# atb.login_and_scrape_page(booking_url, payload=LOGIN_PAYLOAD)


import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.midsussexgolfclub.co.uk/memberbooking/?date=27-02-2023").text
soup = BeautifulSoup(response, 'html.parser')

print(soup)