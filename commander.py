'''Module responsible for defining commander classes'''
from parsers import VideoParser, PlaylistParser
from scrapers import RequestsScraper

class Commander:
    '''Class responsible for orchestrating youtube/scraper functionality'''
    _scrapers = {}
    _targets = {}

    def __init__(self, scraper=None, target=None):
        if scraper and target:
            self.set_scraper(scraper)
            self.set_target(target)

    def set_scraper(self, scraper):
        '''Setting scraper and making sure to use the same object if already used'''
        if scraper in Commander._scrapers.keys():
            self.scraper = Commander._scrapers[scraper]
        else:
            if 'requests' in scraper:
                self.scraper = RequestsScraper()

            Commander._scrapers[scraper] = self.scraper

    def set_target(self, target):
        '''Setting target and making sure to use the same object if already used'''
        if target in Commander._targets.keys():
            self.target = Commander._targets[target]
        else:
            if 'video' in target:
                self.target = VideoParser()
            elif 'playlist' in target:
                self.target = PlaylistParser()

            Commander._targets[target] = self.target

    def extract_data(self, url):
        '''Method used for requesting and returning video details

        Args:
            url (string): Link to the webpage

        Returns:
            [unnamed]: Video details
        '''
        self.scraper.make_request(url)
        return self.target.parse_data(self.scraper.get_text())
