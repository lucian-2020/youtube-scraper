'''Module responsible for defining Youtube objects'''
import json

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

from soup_paths import REQUEST_VIDEO_PATHS as RVP
from soup_paths import REQUEST_PLAYLIST_PATHS as RPP

class DataProcessor(ABC):
    '''Blueprint for Processor classes'''
    def __init__(self):
        self.current_data = None

    @abstractmethod
    def parse(self, source):
        '''Method used for parsing data'''

    @abstractmethod
    def display(self):
        '''Method used displaying current data'''

    @abstractmethod
    def save(self):
        '''Method used for saving data to disk'''


class VideoDP(DataProcessor):
    '''Class used for processing Youtube video data'''

    def parse(self, source):
        '''Method used for parsing html and saving data to object

        Args:
            source (string): Full webpage

        Modifies:
            self.current_data (dictionary): Current data
        '''
        soup = BeautifulSoup(source, 'html.parser')
        video_details = {}

        for item in list(RVP.keys()):
            video_details[item] = soup.findAll(RVP[item]['tag'],
                                               RVP[item]['attrs'])[0].text.strip()
        video_details['channel_name'] = json.loads(video_details['channel_name'])\
['itemListElement'][0]['item']['name']

        for detail in ['likes', 'dislikes', 'number_of_views']:
            video_details[detail] = ''.join(digit for digit in \
video_details[detail] if digit.isdigit())

        self.current_data = video_details

    def display(self):
        '''Method used for displaying current object data'''
        for key, value in self.current_data.items():
            print(f'{key}: {value}\n')

    def save(self):
        '''Method used for saving data to disk'''


class PlaylistDP(DataProcessor):
    '''Class used for processing Youtube playlist data'''

    def parse(self, source):
        '''Method used for parsing html and saving data to object

        Args:
            source (string): Full webpage

        Modifies:
            self.video_list (list): Current videos in playlist
        '''
        soup = BeautifulSoup(source, 'html.parser')
        video_list = []

        for link in soup.findAll(RPP['link']['tag'], RPP['link']['attrs']):
            partial_link = link.get('href').split('&')[0]
            full_link = ''.join(['https://www.youtube.com', partial_link])
            video_list.append(full_link)

        self.current_data = video_list

    def display(self):
        '''Method used for displaying current object data'''
        for video in self.current_data:
            print(video)

    def save(self):
        '''Method used for saving data to disk'''
