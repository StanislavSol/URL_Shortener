from urllib.parse import unquote
import pyshorteners
import validators
import requests


URL_START_INDEX = 4


def normalize_url(data):
    url_parse = unquote(unquote(data[URL_START_INDEX:]))
    return url_parse


def get_short_url(url):
    short_url = pyshorteners.Shortener()
    return short_url.tinyurl.short(url)


def get_error(url):
    error = {}

    if not url:
        return {'message': 'URL обязателен', 'category': 'danger'}
    if not validators.url(url):
        return {'message': 'Некорректный URL', 'category': 'danger'}
    try:
        request = requests.get(url)
    except requests.ConnectionError:
        return {'message': 'Некорректный URL', 'category': 'danger'}

    return error
