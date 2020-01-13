'''Module responsible for defining scrapers'''
from abc import ABC, abstractmethod

import requests

class Scraper(ABC):
    '''Blueprint for Scraper classes'''
    @abstractmethod
    def get_request(self, url):
        '''Method used for making a GET request at the url parameter'''
    
    @property
    @abstractmethod
    def text(self):
        '''Method used for returning the HTML of a request'''


class RequestsScraper(Scraper):
    '''
    Class used for scraping YouTube videos using the requests library

    Attributes:
        headers (dict): Stores headers used in GET requests
        response (request object): Null until GET request
    '''
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language':'en-US'}
        self.response = None

    def get_request(self, url):
        '''Method used for making a GET request at the url parameter

        Args:
            url (string): Link to the webpage
        '''
        self.response = requests.get(url, headers=self.headers)
    
    @property
    def text(self):
        '''Method used for returning the HTML of a a request

        Returns:
            self.text (string): Webpage HTML
        '''
        return self.response.text
