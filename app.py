'''Base module for YTScraper'''
import json

from bs4 import BeautifulSoup
from soup_paths import REQUEST_VIDEO_PATHS as RVP
from scraper import RequestsScraper

class Video:
    '''
    Class used for scraping YouTube videos
    '''
    def __init__(self):
        pass

    @staticmethod
    def parse_data(source):
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

        return video_details

    @staticmethod
    def get_data(url, scraper):
        '''Method used for requesting and returning video details

        Args:
            url (string): Link to the webpage
            scraper (object): Instance of a Scraper class

        Returns:
            [unnamed] (dictionary): Video details specified in VSP
        '''

        if isinstance(scraper, RequestsScraper):
            scraper.make_request(url)
            return Video.parse_data(scraper.get_text())

        raise Exception("Please pass an instance of a scraper class")

if __name__ == '__main__':
    VIDEO_LINK = input('Please input a full YouTube video link:\n')
    SCRAPER = RequestsScraper()
    VIDEO_DETAILS = Video.get_data(VIDEO_LINK, SCRAPER)

    for key, value in VIDEO_DETAILS.items():
        print(f'The {key} is {value}')
