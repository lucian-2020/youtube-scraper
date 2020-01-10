"""Base module for YTScraper"""
import json
import requests

from bs4 import BeautifulSoup


# Dictionary containing BeautifulSoup paths for video details
VSP = {
    'title':{'tag': 'span',
             'attrs': {'class': 'watch-title'}},
    'channel_name': {'tag':'script',
                     'attrs': {'type': 'application/ld+json'}},
    'number_of_views': {'tag': 'div',
                        'attrs': {'class': 'watch-view-count'}},
    'likes': {'tag': 'button',
              'attrs': {'title': 'I like this'}},
    'dislikes': {'tag': 'button',
                 'attrs': {'title': 'I dislike this'}},
    'channel_subcount': {'tag': 'span',
                         'attrs': {'class': 'yt-subscription-button-subscriber\
-count-branded-horizontal yt-subscriber-count'}}
}


class VideoScraper:
    '''
    Class used for scraping YouTube videos

    Attributes:
        headers (dict): Stores headers used in GET requests
    '''
    def __init__(self, headers=None):
        self.headers = headers if headers else \
{'User-Agent': 'Mozilla/5.0', 'Accept-Language':'en-US'}

    def get_videohtml(self, url):
        '''Method used for returning the HTML of a webpage

        Args:
            url (string): Link to the webpage

        Returns:
            webpage.text (string): Webpage HTML
        '''
        webpage = requests.get(url, headers=self.headers)
        return webpage.text

    @staticmethod
    def parse_videodata(source):
        '''Method used for parsing html and returning relevant video details

        Args:
            source (string): Full webpage

        Returns:
            video_details (dictionary): Video details specified in VSP
        '''
        soup = BeautifulSoup(source, 'html.parser')
        video_details = {}

        for item in list(VSP.keys()):
            video_details[item] = soup.findAll(VSP[item]['tag'], VSP[item]['attrs'])[0].text.strip()

        video_details['channel_name'] = json.loads(video_details['channel_name'])\
['itemListElement'][0]['item']['name']

        return video_details

    def get_videodetails(self, url):
        '''Method used for requesting and returning video details

        Args:
            url (string): Link to the webpage

        Returns:
            [unnamed] (dictionary): Video details specified in VSP
        '''
        return VideoScraper.parse_videodata(self.get_videohtml(url))


if __name__ == '__main__':
    VIDEO_LINK = input('Please input a full video link:\n')
    SCRAPER = VideoScraper()
    VIDEO_DETAILS = SCRAPER.get_videodetails(VIDEO_LINK)

    for key, value in VIDEO_DETAILS.items():
        print(f'The {key} is {value}')
