#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sherry Lin'
SITENAME = 'Solring Lin'
SITEURL = ''

THEME= '../Flex/'
#THEME= '/Users/solring/GitWorkspace/Flex/'
#THEME= '/Users/solring/GitWorkspace/nest/'
#THEME= '/Users/solring/GitWorkspace/pelican-clean-blog/'

PATH = 'content'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'Chinese (Traditional)'

# Flex configs
MAIN_MENU = True
SITETITLE = 'SOLRING LIN'
SITESUBTITLE = 'Software Developer | Technical notes and everything'
SITEDESCRIPTION= 'Technical notes and everything.'
SITELOGO = 'images/profile.jpg'
#FAVICON = 'images/favicon.ico'
PYGMENTS_STYLE = 'monokai'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('About', '/about.html'),
         ('Resume', 'https://www.linkedin.com/in/sherry-lin-73312843/'),
         ('sherry12714@gmail.com', '#'))

# Social widget
SOCIAL = (('github', 'http://github.com/solring'),
          ('linkedin', 'https://www.linkedin.com/in/sherry-lin-73312843/'),
          ('twitter', 'http://twitter.com/solringlin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
