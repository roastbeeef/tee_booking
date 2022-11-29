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