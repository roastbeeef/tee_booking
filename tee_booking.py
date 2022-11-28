import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

from src.credentials import USERNAME, PASSWORD
from src.vars import full_auth_url, full_booking_url
from src.funcs import system_log_in

# TODO: get basic tee booking working using selenium chromedriver
# TODO: make headless
# TODO: schedule on AWS lambda
# TODO: create web front-end
# TODO: allow user log-in
# TODO: allow scheduling for now or at soonest available point

# dynamic variables
booking_date = str("29-11-2022")

# setting up the chrome webdriver
DRIVER = webdriver.Chrome(executable_path = r'../resources/chromedriver')

# logging in to the webpage
system_log_in(DRIVER, full_auth_url, USERNAME, PASSWORD)


def get_time_to_book(desired_tee_date, 
                     desired_tee_time, 
                     days_in_advance,
                     available_time):
    # this function will get the time to book based on the soonest available booking date
    # will be x days before desired booking datetime and at y time (the moment the booking system opens)
    ...

def check_log_in_status():
    # checks whether a user is logged in or not
    ...

def system_log_out():
    # function to log out to the system
    ...



def get_available_tee_times(_soup):
    """
    Function to return a list of all currently available tee times.
    Params:
        soup: str
    Returns:
        tee_times_list: List of currently available tee times
    """
    time_length = 5
    tee_times_list = []
    for available_tee_time in _soup.find_all('td', re.compile("^bookable")):
        tee_times_list.append(available_tee_time.get_text()[:time_length])
    return tee_times_list

def book_tee_time():
    # function to actually book a tee time based on the desired date
    ...

def add_users_to_tee_time():
    # function to add users to tee time
    ...

tee_times_list = get_available_tee_times(soup)
print(tee_times_list)


# get the tee times and create a dictionary of the tee times and the item IDs
# linking directly through using the item id wont work, niether will the link. have to save the datetime and then


# for available_tee_time in soup.find_all('td', 'data-date="29-11-2022"'):
#     # display the actual urls
#     print(available_tee_time.get())  





# print(soup)