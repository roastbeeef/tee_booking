import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select



# dynamic
booking_date = str("29-11-2022")

# static
url_base = "https://www.midsussexgolfclub.co.uk/"
url_booking_ext = f"memberbooking/?date={booking_date}"
url_authentication = ""

	
## create an object of the chrome webdriver
driver = webdriver.Chrome(executable_path = r'../resources/chromedriver')
driver.get('https://www.selenium.dev/')

def get_html_document(url):
    """
    Function to return the websites soup
    Params:
        url: URL of website to scrape
    Returns:
        response: BS4 soup output
    """
    response = requests.get(url)
    return response.text

html_document = get_html_document(url_base+url_booking_ext)
soup = BeautifulSoup(html_document)

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

def system_log_in():
    # function to log in to the system
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