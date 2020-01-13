'''Module responsible for defining commander classes'''
from dataprocessors import VideoDP, PlaylistDP
from scrapers import RequestsScraper

class Commander:
    '''Class responsible for orchestrating parsers/scrapers functionality'''
    _scrapers_pool = {'requests':RequestsScraper}
    _dataprocessors_pool = {'video':VideoDP, 'playlist': PlaylistDP}

    _scrapers = {}
    _dataprocessors = {}

    def __init__(self, scraper=None, dataprocessor=None):
        if scraper and targets:
            self.set_scraper(scraper)
            self.set_dataprocessor(dataprocessor)

    def set_scraper(self, scraper):
        '''Setting scraper and making sure to use the same object if already used'''
        if scraper in Commander._scrapers.keys():
            self.scraper = Commander._scrapers[scraper]
        else:
            self.scraper = Commander._scrapers_pool[scraper]()
            Commander._scrapers[scraper] = self.scraper

    def set_dataprocessor(self, dataprocessor):
        '''Setting target and making sure to use the same object if already used'''
        if dataprocessor in Commander._dataprocessors.keys():
            self.dataprocessor = Commander._dataprocessors[dataprocessor]
        else:
            self.dataprocessor = Commander._dataprocessors_pool[dataprocessor]()
            Commander._dataprocessors[dataprocessor] = self.dataprocessor

    def extract_data(self, url):
        '''Method used for requesting and returning video details

        Args:
            url (string): Link to the webpage

        Returns:
            [unnamed]: Video details
        '''
        self.scraper.make_request(url)
        return self.dataprocessor.parse_data(self.scraper.get_text())
