'''Base module for YTScraper'''
from commander import Commander

if __name__ == '__main__':
    REQUEST_NO = int(input('Number of requests: '))

    COMMANDER = Commander()

    for i in range(REQUEST_NO):
        INPUT = input('Please input a full YouTube video/playlist link:\n')

        if 'playlist' in INPUT:
            COMMANDER.set_target('playlist')
            COMMANDER.set_scraper('requests')
            DATA = COMMANDER.extract_data(INPUT)

        elif 'watch' in INPUT:
            COMMANDER.set_target('video')
            COMMANDER.set_scraper('requests')
            DATA = COMMANDER.extract_data(INPUT)

        COMMANDER.target.display_data()
