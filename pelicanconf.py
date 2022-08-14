#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = "Yassine Belmamoun"
SITEURL = "http://localhost:8000"

PATH = "content"
OUTPUT_PATH = "output/"

TIMEZONE = "Asia/Bangkok"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/belmamoun-yassine/"),
    ("github", "http://www.github.com/yassinebelmamoun"),
    ("facebook", "https://www.facebook.com/yassine.belmamoun"),
    ("envelope", "mailto:belmamoun.yassine@gmail.com"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# --------------------
# Custom configuration for Flex theme
# Description: https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
# Example: https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example
# --------------------

# Default Theme
THEME = "/Users/yassine/Documents/repos/pelican-themes/Flex"

PLUGIN_PATHS = ["/Users/yassine/Documents/repos/pelican-plugins"]
PLUGINS = ["post_stats"]


SITENAME = "Yassine Belmamoun - Personal Website"
SITETITLE = "Yassine Belmamoun"
SITESUBTITLE = "Tech entrepreneur & Software engineer"
SITELOGO = SITEURL + "/images/profile_picture_002.jpg"
FAVICON = SITEURL + "/images/favicon/favicon.ico"

SITEDESCRIPTION = "Yassine Belmamoun - Software Engineer & Tech Entrepreneur"
BROWSER_COLOR = "#4285f4"
ROBOTS = "index, follow"
HOME_HIDE_TAGS = True

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}
COPYRIGHT_YEAR = datetime.now().year

DATE_FORMATS = {
    "en": "%B %d, %Y",
}


MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

HOME_HIDE_TAGS = True
FEED_ALL_ATOM = "feeds/all.atom.xml"

# all PYGMENTS styles are here: https://github.com/alexandrevicenzi/Flex/tree/master/static/pygments
PYGMENTS_STYLE = "manni"

LINKS_IN_NEW_TAB = "external"
USE_FOLDER_AS_CATEGORY = True

# USE_LESS = True
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/CNAME": {"path": "CNAME"},
}
CUSTOM_CSS = "static/custom.css"
