'''Module responsible for defining commander classes'''
from dataprocessors import VideoDP, PlaylistDP
from scrapers import RequestsScraper

class Commander:
    '''Class responsible for orchestrating dataprocessors/scrapers functionality'''
    _scrapers_pool = {'requests': RequestsScraper}
    _dataprocessors_pool = {'video': VideoDP, 'playlist': PlaylistDP}

    _scrapers = {}
    _dataprocessors = {}

    def __init__(self, scraper=None, dataprocessor=None):
        if scraper and dataprocessor:
            self.set_scraper(scraper)
            self.set_dataprocessor(dataprocessor)
        self.set_dispatcher()

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

    def set_dispatcher(self):
        '''Setts dispatcher dictionary responsible for command logic'''
        self._dispatcher = {
            'type': lambda x: self.set_dataprocessor(x)\
             if x in Commander._dataprocessors_pool.keys() else None,
            'scraper': lambda x: self.set_scraper(x)\
             if x in Commander._scrapers_pool.keys() else None,
            'link': lambda x: self.scraper.get_request(x) if x else None,
            'parse': lambda x: self.dataprocessor.parse_data(self.scraper.text) if x else None,
            'clean': lambda x: self.dataprocessor.clean_data() if x else None,
            'display': lambda x: self.dataprocessor.display_data() if x else None}

    def execute(self, command):
        '''Executes given command using dispatcher'''
        for item, value in command.items():
            self._dispatcher[item](value)
