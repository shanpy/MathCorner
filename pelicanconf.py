#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pengyin Shan'
SITENAME = u'Pengyin Shan and Math, Finance, Statistics'
SITEURL = 'http://shanpy.github.io/mathcorner'

DESCRIPION = 'A corner for Pengyin Shan to record her thoughs in Math, Finance and Statistics'
SITE_DESCRIPION = 'A corner for Pengyin Shan to record her thoughs in Math, Finance and Statistics'
SITESUBTITLE = 'Alway Learning. Getting Things Done.'
EMAIL = 'shanpy901115@gmail.com'
TIMEZONE = 'America/New_York'
FOOTER = 'Alway Learning. Getting Things Done.'
FAVICON = './images/favicon.ico'
FAVICON_TYPE = 'image/x-icon'

PATH = 'content'

STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/CNAME', 'notebooks', 'code']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/favicon.ico': {'path': 'favicon.ico'}}

GITHUB_URL = 'https://github.com/shanpy/mathcorner'

#PLUGINS
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
			'sitemap', 
			'extract_toc', 
			'tipue_search',
           	'neighbors', 
           	'render_math', 
           	'related_posts', 
           	'assets', 
           	'share_post',
           	'multi_part',
			'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 
			'liquid_tags.vimeo', 'liquid_tags.include_code', 'liquid_tags.notebook',
			]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}		
#Liquid Tags
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read()
CODE_DIR = 'code'

#Markup Setting
MARKUP = ('md', 'rst')	

#THEME
THEME = 'themes/alchemy'
BOOTSWATCH = 'darkly'
PYGMENTS = 'monokai'
NAVBAR_INVERSE = 'true'
LANDING_PAGE = 'http://pengyin-shan.com'

TYPOGRIFY = True
PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True
ARCHIVES_ON_MENU = True
#PROFILE_IMAGE = './images/profile.png'
SHOW_ARTICLE_AUTHOR = True
SITE_SUBTEXT = 'A corner for Pengyin Shan to record her thoughs in Math, Finance and Statistics'
EMAIL_ADDRESS = 'shanpy901115@gmail.com'
GITHUB_ADDRESS = 'https://github.com/shanpy'

RECENT_ARTICLES_COUNT = 5 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('My Technical Blog', 'http://pengyin-shan.com/blogcode'),
         )

SOCIAL = (
	('My Linkedin', 'https://www.linkedin.com/in/pengyinshan'), 
    #('Github', 'https://github.com/shanpy'),
	)
# Share
SHARE = True

#COMMENT 
DISQUS_SITENAME = 'Pengyin Shan and Math, Finance, Statistics'
DISQUS_SHORTNAME = 'pengyinblog'


DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
