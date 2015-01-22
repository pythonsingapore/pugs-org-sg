#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'webmaster'
SITENAME = u'Python User Group Singapore'
SITEURL = ''

# default text in the footer
COPYRIGHT = u'Copyright &copy; 2009 &ndash; 2015, Python User Group Singapore'

DEFAULT_LANG = u'en'
TIMEZONE = 'Asia/Singapore'

THEME = 'theme/pugs_zf'

AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_SAVE_AS = 'author/{slug}.html'

DISPLAY_PAGES_ON_MENU = False  # see MENUITEMS
DEFAULT_PAGINATION = False

# ARTICLE_URL = 'articles/{slug}'
# ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# CATEGORY_URL = 'category/{slug}'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# TAG_URL = 'tag/{slug}'
# TAG_SAVE_AS = 'tag/{slug}/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = [
    ('About', '/pages/about.html'),
    ('Bylaws', '/pages/bylaws.html'),
    ('Organization', '/pages/org.html'),
]

LINKS = (
    ('Mailing list', 'https://groups.google.com/forum/#!forum/pythonsg'),
    ('PUGS on FB', 'https://www.facebook.com/groups/pythonsg/'),
    ('PyCon.SG', 'http://pycon.sg/'),
    ('Python.org', 'http://python.org/'),
)

STATIC_PATHS = [
    'CNAME',
    'img'
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GOOGLE_ANALYTICS = 'UA-46193746-3'
