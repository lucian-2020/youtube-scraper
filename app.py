'''Base module for YTScraper'''
from commander import Commander

if __name__ == '__main__':
    INPUT = input('Please input a full YouTube video/playlist link:\n')
    COMMANDER = Commander()

    if 'playlist' in INPUT:
        PLAYLIST_SETTINGS = {'type': 'playlist',
                             'scraper': 'requests',
                             'link': INPUT,
                             'parse': True,
                             'save': True,
                             'display': False}
        COMMANDER.execute(PLAYLIST_SETTINGS)

        VIDEO_SETTINGS = {'type': 'video',
                          'scraper': 'requests',
                          'link': '',
                          'parse': True,
                          'save': True,
                          'display': True}

        for video in COMMANDER.dataprocessor.current_data:
            VIDEO_SETTINGS['link'] = video
            COMMANDER.execute(VIDEO_SETTINGS)

    elif 'watch' in INPUT:
        VIDEO_SETTINGS = {'type': 'video',
                          'scraper': 'requests',
                          'link': '',
                          'parse': True,
                          'save': True,
                          'display': True}
        COMMANDER.execute(VIDEO_SETTINGS)
