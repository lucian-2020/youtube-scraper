'''Base module for YTScraper'''
import json
import requests

from bs4 import BeautifulSoup


# VideoSoupPaths contains paths for video details
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
-count-branded-horizontal yt-subscriber-count'}}}


class RequestsScraper:
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
        '''Method used for returning the HTML of a webpage

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


class Video:
    '''
    Class used for scraping YouTube videos

    Attributes:
        headers (dict): Stores headers used in GET requests
        scraper (RequestsScraper):
    '''
    def __init__(self, scrape_with='requests'):
        if scrape_with == 'requests':
            self.scraper = RequestsScraper()

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
            video_details[item] = soup.findAll(VSP[item]['tag'],
                                               VSP[item]['attrs'])[0].text.strip()

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
        self.scraper.make_request(url)
        return Video.parse_videodata(self.scraper.get_text())


if __name__ == '__main__':
    VIDEO_LINK = input('Please input a full YouTube video link:\n')
    VIDEO_DETAILS = Video().get_videodetails(VIDEO_LINK)

    for key, value in VIDEO_DETAILS.items():
        print(f'The {key} is {value}')
        