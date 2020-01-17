'''Module responsible for defining commander classes'''
from dataprocessors import VideoDP, PlaylistDP
from scrapers import RequestsScraper
from recommenders import SimpleRecommender

class Commander:
    '''Class responsible for orchestrating dataprocessors/scrapers functionality'''
    scrapers_pool = {'requests': RequestsScraper}
    dataprocessors_pool = {'video': VideoDP, 'playlist': PlaylistDP}
    recommenders_pool = {'simple': SimpleRecommender}

    scrapers = {}
    dataprocessors = {}
    recommenders = {}

    def __init__(self):
        self.set_dispatcher()
        
    def set(self, res, value):
        '''Setting resource and making sure to use cache if already instantiated'''
        res_dict = getattr(Commander, ''.join([res, 's']))
        res_pool = getattr(Commander, ''.join([res, 's_pool']))
        
        if value in res_dict.keys():
            setattr(self, res, res_dict[value])
        else:
            setattr(self, res, res_pool[value]())
            res_dict[value] = getattr(self, res)

    def set_dispatcher(self):
        '''Sets dispatcher dictionary and self variables'''
        self.dataprocessor, self.scraper, self.recommender = (None, None, None)
        self._dispatcher = {
            'set_dataprocessor': lambda x: self.set('dataprocessor', x),
            'set_scraper': lambda x: self.set('scraper', x),
            'link': lambda x: self.scraper.get(x) if x else None,
            'parse': lambda x: self.dataprocessor.parse(self.scraper.text) if x else None,
            'save': lambda x: self.dataprocessor.save() if x else None,
            'display': lambda x: self.dataprocessor.display() if x else None,
            'set_recommender': lambda x: self.set('recommender', x) if x else None,
            'recommend': lambda x: self.recommender.append(\
self.dataprocessor.current_data) if x else None}

    def execute(self, command):
        '''Executes given command using dispatcher'''
        for item, value in command.items():
            self._dispatcher[item](value)

    def recommend(self):
        '''Makes recommendation based on current recommender values'''
        self.recommender.recommend()
