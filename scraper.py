'''Module responsible for defining scrapers'''
from abc import ABC, abstractmethod

import requests

class Scraper(ABC):
    '''Blueprint for Scraper classes'''
    @abstractmethod
    def make_request(self, url):
        '''Method used for making a GET request at the url parameter'''

    @abstractmethod
    def get_text(self):
        '''Method used for returning the HTML of a request'''


class RequestsScraper(Scraper):
    '''
    Class used for scraping YouTube videos using the requests library

    Attributes:
        headers (dict): Stores headers used in GET requests
        params (dict): Stores other parameters used in GET requests
        response (request object): Null until GET request
    '''
    def __init__(self, headers=None, params=None):
        self.headers = headers if headers else \
{'User-Agent': 'Mozilla/5.0', 'Accept-Language':'en-US'}
        self.params = params
        self.response = None

    def make_request(self, url):
        '''Method used for making a GET request at the url parameter

        Args:
            url (string): Link to the webpage
        '''
        self.response = requests.get(url, headers=self.headers, params=self.params)

    def get_text(self):
        '''Method used for returning the HTML of a a request

        Returns:
            self.text (string): Webpage HTML
        '''
        return self.response.text
