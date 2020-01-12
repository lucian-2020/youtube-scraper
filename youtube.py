'''Module responsible for defining Youtube objects'''
import json
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from soup_paths import REQUEST_VIDEO_PATHS as RVP
from soup_paths import REQUEST_PLAYLIST_PATHS as RPP
from scraper import RequestsScraper

class YoutubeWebPage(ABC):
    '''Blueprint for Youtube classes'''
    def __init__(self, scrape_with, **kwargs):
        if scrape_with == 'requests':
            self.scraper = RequestsScraper(kwargs)

        self.current_data = None

    @abstractmethod
    def parse_data(self, source):
        '''Method used for parsing and returning data'''

    @abstractmethod
    def display_data(self):
        '''Method used displaying current object data'''

    def get_data(self, url):
        '''Method used for requesting and returning video details

        Args:
            url (string): Link to the webpage
            scraper (object): Instance of a Scraper class

        Returns:
            [unnamed] (dictionary): Video details specified in VSP
        '''

        if isinstance(self.scraper, RequestsScraper):
            self.scraper.make_request(url)
            return self.parse_data(self.scraper.get_text())

        raise Exception("Please pass an instance of a scraper class")


class Video(YoutubeWebPage):
    '''Class used for scraping a YouTube video'''

    def parse_data(self, source):
        '''Method used for parsing html and returning relevant video details

        Args:
            source (string): Full webpage

        Returns:
            video_details (dictionary): Video details specified in VSP
        '''
        soup = BeautifulSoup(source, 'html.parser')
        video_details = {}

        for item in list(RVP.keys()):
            video_details[item] = soup.findAll(RVP[item]['tag'],
                                               RVP[item]['attrs'])[0].text.strip()

        video_details['channel_name'] = json.loads(video_details['channel_name'])\
['itemListElement'][0]['item']['name']

        self.current_data = video_details

    def display_data(self):
        '''Method used for displaying current object data'''
        for key, value in self.current_data.items():
            print(f'{key}: {value}\n')


class Playlist(YoutubeWebPage):
    '''Class used for scraping a Youtube playlist'''

    def parse_data(self, source):
        '''Method used for parsing html and returning a video list

        Args:
            source (string): Full webpage

        Returns:
            video_list (list): List of youtube videos present in playlist page
        '''
        soup = BeautifulSoup(source, 'html.parser')
        video_list = []

        for link in soup.findAll(RPP['link']['tag'], RPP['link']['attrs']):
            partial_link = link.get('href').split('&')[0]
            full_link = ''.join(['https://www.youtube.com', partial_link])
            video_list.append(full_link)

        self.current_data = video_list

    def display_data(self):
        '''Method used for displaying current object data'''
        for video in self.current_data:
            print(video)
