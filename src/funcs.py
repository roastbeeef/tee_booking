# packages
from selenium.webdriver.common.by import By

def system_log_in(driver: object, 
                  login_page: str, 
                  username: str, 
                  password: str) -> None:
    """
    Function to log in to the website
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