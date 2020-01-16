'''Module responsible for defining commander classes'''
from dataprocessors import VideoDP, PlaylistDP
from scrapers import RequestsScraper
from recommenders import SimpleRecommender

class Commander:
    '''Class responsible for orchestrating dataprocessors/scrapers functionality'''
    _scrapers_pool = {'requests': RequestsScraper}
    _dataprocessors_pool = {'video': VideoDP, 'playlist': PlaylistDP}
    _recommenders_pool = {'simple': SimpleRecommender}

    _scrapers = {}
    _dataprocessors = {}
    _recommenders = {}

    def __init__(self, scraper=None, dataprocessor=None, recommender=None):
        if scraper and dataprocessor and recommender:
            self.set_scraper(scraper)
            self.set_dataprocessor(dataprocessor)
            self.set_recommender(recommender)
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

    def set_recommender(self, recommender):
        '''Setting target and making sure to use the same object if already used'''
        if recommender in Commander._recommenders.keys():
            self.recommender = Commander._recommenders[recommender]
        else:
            self.recommender = Commander._recommenders_pool[recommender]()
            Commander._recommenders[recommender] = self.recommender

    def set_dispatcher(self):
        '''Setts dispatcher dictionary responsible for command logic'''
        self._dispatcher = {
            'set_dataprocessor': lambda x: self.set_dataprocessor(x)\
             if x in Commander._dataprocessors_pool.keys() else None,
            'set_scraper': lambda x: self.set_scraper(x)\
             if x in Commander._scrapers_pool.keys() else None,
            'link': lambda x: self.scraper.get(x) if x else None,
            'parse': lambda x: self.dataprocessor.parse(self.scraper.text) if x else None,
            'save': lambda x: self.dataprocessor.save() if x else None,
            'display': lambda x: self.dataprocessor.display() if x else None,
            'set_recommender': lambda x: self.set_recommender(x) if x else None,
            'recommend': lambda x: self.recommender.append(\
self.dataprocessor.current_data) if x else None}

    def execute(self, command):
        '''Executes given command using dispatcher'''
        for item, value in command.items():
            self._dispatcher[item](value)

    def recommend(self):
        '''Makes recommendation based on current recommender values'''
        self.recommender.recommend()
