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
tee_time_mm = str('00')
tee_time_hh = str('07')
tee_time_str = f'teetime-mins-{tee_time_mm} teetime-hours-{tee_time_hh}'
text_xpath = f'//tr[contains(@class, "{tee_time_str}")]//td'
# clicking on the tee time within the table
driver.find_element(by=By.XPATH, value=text_xpath).click()
# following the page through to book a 4 ball
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="cluetip-inner"]/div[2]/form/em/input').click()




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