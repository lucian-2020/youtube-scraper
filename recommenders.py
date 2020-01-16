'''Module responsible for defining Recommender classes'''
from abc import ABC, abstractmethod

class Recommender(ABC):
    '''Blueprint for Recommender classes'''
    @abstractmethod
    def append(self, data):
        '''Method used for appending data'''

    @abstractmethod
    def recommend(self):
        '''Method used for recommending based on current data'''

class SimpleRecommender(Recommender):
    '''Class used for implementing basic recommender functionality'''

    def __init__(self):
        self.current_data = []

    def append(self, data):
        self.current_data.append(data)

    def recommend(self):
        for index in range(len(self.current_data)):
            if self.current_data[index]['likes'] == 0:
                self.current_data[index]['likes'] = 1
            if self.current_data[index]['dislikes'] == 0:
                self.current_data[index]['dislikes'] = 1

            self.current_data[index]['ratio'] = self.current_data[index]['likes']\
 / self.current_data[index]['dislikes']


        data = sorted(self.current_data, key=lambda x: x['ratio'], reverse=True)
        for index in range(10):
            print(data[index]['title'])
