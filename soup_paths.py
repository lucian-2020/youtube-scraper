'''Module responsible for defining BeautifulSoup paths'''
REQUEST_VIDEO_PATHS = {
    'title':{'tag': 'span',
             'attrs': {'class': 'watch-title'}},
    'channel_name': {'tag':'script',
                     'attrs': {'type': 'application/ld+json'}},
    'number_of_views': {'tag': 'div',
                        'attrs': {'class': 'watch-view-count'}},
    'likes': {'tag': 'button',
              'attrs': {'title': 'I like this'}},
    'dislikes': {'tag': 'button',
                 'attrs': {'title': 'I dislike this'}}
}

REQUEST_PLAYLIST_PATHS = {
    "link":{"tag":"a",
            "attrs":{"class": "pl-video-title-link yt-uix-tile-link\
 yt-uix-sessionlink spf-link"}}
}
