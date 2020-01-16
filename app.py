'''Base module for YTScraper'''
from commander import Commander

if __name__ == '__main__':
    INPUT = input('Please input a full YouTube video/playlist link:\n')
    COMMANDER = Commander()

    if 'playlist' in INPUT:
        COMMANDER_SETTINGS = {'set_dataprocessor': 'playlist',
                              'set_scraper': 'requests'}
        COMMANDER.execute(COMMANDER_SETTINGS)

        PLAYLIST_SETTINGS = {'link': INPUT,
                             'parse': True,
                             #'save': True,
                             'display': False}
        COMMANDER.execute(PLAYLIST_SETTINGS)
        DATA = COMMANDER.dataprocessor.current_data

        COMMANDER_SETTINGS = {'set_dataprocessor': 'video',
                              'set_scraper': 'requests',
                              'set_recommender': 'simple'}
        COMMANDER.execute(COMMANDER_SETTINGS)

        VIDEO_SETTINGS = {'link': '',
                          'parse': True,
                          #'save': True,
                          'display': False,
                          'recommend': True}
        for video in DATA:
            VIDEO_SETTINGS['link'] = video
            COMMANDER.execute(VIDEO_SETTINGS)

        COMMANDER.recommend()

    elif 'watch' in INPUT:
        COMMANDER_SETTINGS = {'set_dataprocessor': 'video',
                              'set_scraper': 'requests'}
        COMMANDER.execute(COMMANDER_SETTINGS)

        VIDEO_SETTINGS = {'link': INPUT,
                          'parse': True,
                          'save': True,
                          'display': True}
        COMMANDER.execute(VIDEO_SETTINGS)
