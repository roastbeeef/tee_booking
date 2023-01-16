## THIS FILE IS THE AUTOMATION SCRIPT

import time
from selenium import webdriver

from src.credentials import USERNAME, PASSWORD
from src.vars import FULL_AUTH_URL, FULL_BOOKING_URL
from src.funcs import (
        system_log_in, 
        parse_html,
        get_available_tee_times
        )

# setting up the chrome webdriver
driver = webdriver.Chrome(executable_path = r'../resources/chromedriver')

# logging in to the webpage
system_log_in(driver, FULL_AUTH_URL, USERNAME, PASSWORD)

# TODO: booking date is to become a parameter later on
BOOKING_DATE = '29-11-2022'
BOOKING_URL_WITH_DATE = f'{FULL_BOOKING_URL}{BOOKING_DATE}'
# parsing the HTML and getting a list of the available tee times. this wont be used now, but will be later on to validate
parsed_html = parse_html(BOOKING_URL_WITH_DATE)

# getting the available tee times - this is beyond MVP but will leave here for later
available_tee_times = get_available_tee_times(parsed_html)

from selenium.webdriver.common.by import By
driver.get(BOOKING_URL_WITH_DATE)
time.sleep(1)
tee_time_mm = str('00')
tee_time_hh = str('07')
tee_time_str = f'teetime-mins-{tee_time_mm} teetime-hours-{tee_time_hh}'
text_xpath = f'//tr[contains(@class, "{tee_time_str}")]//td//a'
# clicking on the tee time within the table
driver.find_element(by=By.XPATH, value=text_xpath).click()
# following the page through to book a 4 ball
driver.find_element(by=By.XPATH, value='//*[@id="cluetip-inner"]/div[2]/form/em/input').click()
time.sleep(1)
driver.get(BOOKING_URL_WITH_DATE)


# use this to ensure the page loads
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# timeout = 5
# driver.get(BOOKING_URL_WITH_DATE)
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'element_id'))
#     WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print("Timed out waiting for page to load")

def check_log_in_status():
    # checks whether a user is logged in or not
    ...

def system_log_out():
    # function to log out to the system
    ...





def book_tee_time():
    # function to actually book a tee time based on the desired date
    ...

def add_users_to_tee_time():
    # function to add users to tee time
    ...

# tee_times_list = get_available_tee_times(soup)
# print(tee_times_list)


# get the tee times and create a dictionary of the tee times and the item IDs
# linking directly through using the item id wont work, niether will the link. have to save the datetime and then


# for available_tee_time in soup.find_all('td', 'data-date="29-11-2022"'):
#     # display the actual urls
#     print(available_tee_time.get())  





# print(soup)


# TODO: get basic tee booking working using selenium chromedriver - check
# TODO: make headless
# TODO: schedule on AWS lambda
# TODO: create ci/cd pipeline
# TODO: create web front-end
# TODO: allow user log-in
# TODO: allow scheduling for now or at soonest available point
# TODO: dynamic scheduling. 10 days in advance


from tee_booking.src.funcs import AdvanceTeeBooking
from tee_booking.src.vars import url_base
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True
cdriver = webdriver.Chrome(executable_path = r'../resources/chromedriver', options=chrome_options)


atb = AdvanceTeeBooking(webdriver_loc=cdriver, url=url_base)

atb.system_log_in(username='mattwilsn@gmail.com', password='6503', login_page='login.php')

cdriver.quit()



2


from bs4 import BeautifulSoup as bs4
import requests
import ssl
ssl.match_hostname = lambda cert, hostname: True

usr_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

URL = 'http://midsussexgolfclub.co.uk/'
LOGIN_ROUTE = 'login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 
    'origin': URL, 
    'referer': URL + LOGIN_ROUTE}


s = requests.session()
login_req = s.post(URL + LOGIN_ROUTE, headers=LOGIN_HEADERS, data=LOGIN_PAYLOAD)

print(login_req.status_code)


