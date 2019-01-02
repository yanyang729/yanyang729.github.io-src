#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yang Yang'
SITENAME = u"Yang Yang's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'Keep calm and drink coffe'
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

THEME = 'Flex'

PATH = 'content'
TIMEZONE = 'America/Halifax'
DEFAULT_LANG = u'en'
I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False
# HOME_HIDE_TAGS = True

MENUITEMS = (('Home','/index.html'),
			 ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/yang-yang-105344aa/'),
          ('github', 'https://github.com/yanyang729'),
          ('twitter', 'https://twitter.com/yangyang729729'))


CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017
DEFAULT_PAGINATION = 10


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False


PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}


DISQUS_SITENAME = "yangyang729"
ADD_THIS_ID = 'ra-55adbb025d4f7e55'

STATUSCAKE = {
    'trackid': 'SL0UAgrsYP',
    'days': 7,
    'rumid': 6852,
    'design': 6,
}

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = False



# # here is the ads!
# GOOGLE_ADSENSE = {
#     'ca_id': 'ca-pub-6625957038449899',
#     'page_level_ads': False,
#     'ads': {
#         'aside': '5340595560',
#         'main_menu': '',
#         'index_top': '',
#         'index_bottom': '9584371569',
#         'article_top': '',
#         'article_bottom': '7257980762',
#     }
# }


# Blogroll
# LINKS = (('On my way to data science, I will share notes and tips here. ','#'),
# 	('Hope it will be helpful :) ','#'))
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
