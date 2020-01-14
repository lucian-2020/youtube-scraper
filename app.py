'''Base module for YTScraper'''
from commander import Commander

if __name__ == '__main__':
    INPUT = input('Please input a full YouTube video/playlist link:\n')
    COMMANDER = Commander()

    if 'playlist' in INPUT:
        COMMAND = {'type': 'playlist',
                   'scraper': 'requests',
                   'link': INPUT,
                   'parse': True,
                   'clean': True,
                   'display': True}
        COMMANDER.execute(COMMAND)
        
        COMMAND['type'] = 'video'
        for video in COMMANDER.dataprocessor.current_data:
            COMMAND['link'] = video
            COMMANDER.execute(COMMAND)

    elif 'watch' in INPUT:
        COMMAND = {'type': 'video',
                   'scraper': 'requests',
                   'link': INPUT,
                   'parse': True,
                   'clean': True,
                   'display': True}
        COMMANDER.execute(COMMAND)
