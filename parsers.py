'''Module responsible for defining Youtube objects'''
import json
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from soup_paths import REQUEST_VIDEO_PATHS as RVP
from soup_paths import REQUEST_PLAYLIST_PATHS as RPP

class Parser(ABC):
    '''Blueprint for Youtube classes'''
    def __init__(self):
        self.current_data = None

    @abstractmethod
    def parse_data(self, source):
        '''Method used for parsing and returning data'''

    @abstractmethod
    def display_data(self):
        '''Method used displaying current object data'''


class VideoParser(Parser):
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


class PlaylistParser(Parser):
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