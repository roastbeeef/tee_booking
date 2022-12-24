# packages
import requests
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def system_log_in(driver: object, 
                  login_page: str, 
                  username: str, 
                  password: str) -> None:
    """
    Function to log in to the website.
    Params:
        driver: webdriver (chromdriver) object name
        login_page: url for login page
        username: valid username to log in as
        password: valid password for username
    """
    driver.get(login_page)

    username_field = driver.find_element(by=By.NAME, value='memberid')
    username_field.send_keys(username)

    password_field = driver.find_element(by=By.NAME, value='pin')
    password_field.send_keys(password)

    login_button = driver.find_element(by=By.NAME, value='Submit')
    login_button.click()

    
def get_html_document(url: str) -> str:
    """
    Function to get HTML document (webpage)
    Params:
        url: url of target webpage
    Returns:
        html content of webpage
    """
    response = requests.get(url)

    return response.text

def parse_html(url: str) -> str:
    """
    Function to utilise BS4 to parse the HTML
    Params: 
        url: url to parse
    Returns:
        soup: parsed HTML
    """
    html_document = get_html_document(url)
    soup = BeautifulSoup(html_document, 'html.parser')
    
    return soup


def get_available_tee_times(_soup: str) -> list:
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


## DEPRECATED, REMOVE WHEN POSSIBLE
# functions to be used by the routes

# retrieve all the names from the dataset and put them into a list
def get_names(source):
    names = []
    for row in source:
        # lowercase all the names for better searching
        name = row["name"].lower()
        names.append(name)
    return sorted(names)

# find the row that matches the id in the URL, retrieve name and photo
def get_actor(source, id):
    for row in source:
        if id == str( row["id"] ):
            name = row["name"]
            photo = row["photo"]
            # change number to string
            id = str(id)
            # return these if id is valid
            return id, name, photo
    # return these if id is not valid - not a great solution, but simple
    return "Unknown", "Unknown", ""

# find the row that matches the name in the form and retrieve matching id
def get_id(source, name):
    for row in source:
        # lower() makes the string all lowercase
        if name.lower() == row["name"].lower():
            id = row["id"]
            # change number to string
            id = str(id)
            # return id if name is valid
            return id
    # return these if id is not valid - not a great solution, but simple
    return "Unknown"
