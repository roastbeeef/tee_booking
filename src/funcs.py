# packages
import requests, re, json, decimal
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


# this needs to be changes so the vars are within the scope of the class
def strip_non_alphanumeric(input_string) -> str:
    """function to strip non alphanumeric from a string"""
    return re.sub(r'[^\w\s]', '', str(input_string))

class AdvanceTeeBooking:
    def __init__(self, webdriver_loc, url):
        self.webdriver = webdriver_loc
        self.url = url

    ig_search_phrase = 'intelligentgolf'
    logged_in = False

    def system_log_out(self):
        """
        function to log out of the website
        """
        self.webdriver.get(f'{self.url}?action=logout')

    def system_log_in(self, 
                      login_page: str, 
                      username: str, 
                      password: str) -> None:
        """
        Function to log in to the website.
        Params:
            driver: webdriver (chromedriver) object name
            login_page: url for login page
            username: valid username to log in as
            password: valid password for username
        """
        # TODO: logic here: if already logged in then do not bother logging in
        login_page = f"{self.url}{login_page}"
        self.webdriver.get(login_page)

        username_field = self.webdriver.find_element(by=By.NAME, value='memberid')
        username_field.send_keys(username)

        password_field = self.webdriver.find_element(by=By.NAME, value='pin')
        password_field.send_keys(password)

        login_button = self.webdriver.find_element(by=By.NAME, value='Submit')
        login_button.click()

        WDW(self.webdriver, 5).until(EC.presence_of_element_located((By.ID, "logoutbtn")))

    def validate_website(self,
                         search_phrase: str=ig_search_phrase) -> bool:
        """
        Function to validate whether the booking site is compatible, i.e. IntelligentGolf
        
        Very dunb function scanning of the login page for mentions of IntelligentGolf
        TODO: make this a bit smarter, maybe not case senstive etc - not required for mvp
        TODO: need to verify that this actually works - not required for mvp
        """
        response_body = self._get_html_document(self.url)
        soup = self._parse_html(response_body)
        result = soup.body.findAll(text=search_phrase)
        return True if len(result) > 0 else False

    def _get_html_document(self,
                           session: object, 
                           url: str) -> str:
        """
        Function to get HTML document (webpage)
        Params:
            url: url of target webpage
        Returns:
            html content of webpage
        """
        if session:
            response = session.get(url=url)
        else:
            response = requests.get(url=url)

        return response.text

    def _parse_html(self, html_response: str) -> str:
        """
        Function to utilise BS4 to parse the HTML
        Params: 
            url: url to parse
        Returns:
            soup: parsed HTML
        """
        soup = BeautifulSoup(html_response, 'html.parser')
        
        return soup

    def _get_html_document_and_parse(self,
                                     url: str):
        """
        Function to get...
        ...is this required?

        TODO: sort out docstring
        """
        html_document = self._get_html_document(url=url)
        return self._parse_html(html_document)

    # this needs to be re-written. think about how to manage the session
    def get_available_tee_times(self, url: str, payload: dict) -> list:
        """
        Function to return a list of all currently available tee times.
        Params:
            soup: str
        Returns:
            tee_times_list: List of currently available tee times
        """
        _soup = self.login_and_scrape_page(url, payload)
        booking_times_list = []
        hh_mm_ss_regex = "([0-1]?\d|2[0-3]):([0-5]?\d)"

        for available_tee_time in _soup.findAll('a', href=True, text='Select'):
            tee_time = re.search(hh_mm_ss_regex, available_tee_time['href']).group(0)
            booking_times_list.append(tee_time)
            
        return booking_times_list

    def login_and_scrape_page(self, url: str, payload: dict) -> str:
        """
        Function to log in and scrape a web page based on the date
        Requres bs4, requests
        Params:
            url: full url of webpage
        """
        with requests.Session() as s:
            s.post(url, data=payload)
            response = s.get(f"{url}").text
        
        return BeautifulSoup(response, 'html.parser')
    
    def create_transaction_id(self, timestamp, username, booking_date, booking_time):
        """function to create an almost-unique transaction ID"""
        return f"{timestamp}{username.upper()}{booking_date}{booking_time}"

    def create_tee_booking_transaction(
        self,
        username: str,
        course_id: str, 
        booking_date: int,
        booking_time: str,
        ) -> dict:
        """function to create a transaction payload"""
        timestamp = datetime.strftime(datetime.today(), format="%Y%m%d%H%M%S")
        return {
            'transaction_id': self.create_transaction_id(timestamp, username, booking_date, booking_time),
            'username': username,
            "course_id": str(course_id),
            "booking_date": int(strip_non_alphanumeric(booking_date)), # this will be converted to a date using the datetime package later
            "booking_time": str(strip_non_alphanumeric(booking_time)) # this can just be 4 digits and can be split later to give the colon in the middle
            }

    def insert_data_into_dynamodb(self, transactions_table_obect: object, payload: dict) -> None:
        transactions_table_obect.put_item(
            Item = payload
        )

    def book_tee_time():
        ...



class DecimalEncoder(json.JSONEncoder):
    """
    decimal encoder used to remove Decimal formatting from Dynamo JSON object
    """
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)




    






