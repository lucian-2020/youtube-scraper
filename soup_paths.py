'''Module responsible for declaring BeautifulSoup paths'''
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
                 'attrs': {'title': 'I dislike this'}},
    'channel_subcount': {'tag': 'span',
                         'attrs': {'class': 'yt-subscription-button-subscriber\
-count-branded-horizontal yt-subscriber-count'}}}
