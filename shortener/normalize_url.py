from urllib.parse import unquote
import pyshorteners


URL_START_INDEX = 4


def normalize_url(data):
    url_parse = unquote(unquote(data[URL_START_INDEX:]))
    return url_parse


def get_short_url(url):
    short_url = pyshorteners.Shortener()
    return short_url.tinyurl.short(url)
