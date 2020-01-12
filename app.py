'''Base module for YTScraper'''
from youtube import Video, Playlist

if __name__ == '__main__':
    INPUT = input('Please input a full YouTube video/playlist link:\n')

    if 'playlist' in INPUT:
        SCRAPER = Playlist(scrape_with='requests')
    elif 'watch' in INPUT:
        SCRAPER = Video(scrape_with='requests')

    SCRAPER.get_data(INPUT)
    SCRAPER.display_data()
