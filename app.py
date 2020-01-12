'''Base module for YTScraper'''
from youtube import Video, Playlist

if __name__ == '__main__':
    INPUT = input('Please input a full YouTube video/playlist link:\n')

    if 'playlist' in INPUT:
        PLAYLIST = Playlist(scrape_with='requests')
        VIDEO_LIST = PLAYLIST.get_data(INPUT)
        for video in VIDEO_LIST:
            print(video)
    elif 'watch' in INPUT:
        VIDEO = Video(scrape_with='requests')
        VIDEO_DETAILS = VIDEO.get_data(INPUT)
        for key, value in VIDEO_DETAILS.items():
            print(f'The {key} is {value}')
