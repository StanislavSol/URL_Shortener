from urllib.parse import unquote
import validators
import requests
from shortener_app.keygen import create_unique_random_key
from shortener_app.crud import get_url


START_INDEX = 4


def normalize_url(data, db):
    url, key = data.split('&')
    url_parse = unquote(unquote(url[START_INDEX:]))
    key_parse = unquote(unquote(key[START_INDEX:]))

    if key_parse:
        return url_parse, key_parse
    else:
        return url_parse, create_unique_random_key(db)


def get_error(url, key, db):
    error = {}

    if not url:
        return {
            'message': 'URL обязателен',
            'category': 'danger',
            'url': url
        }
    if not validators.url(url):
        return {
            'message': 'Некорректный URL',
            'category': 'danger',
            'url': url
        }
    try:
        requests.get(url)
    except requests.ConnectionError:
        return {
            'message': 'Некорректный URL',
            'category': 'danger',
            'url': url
        }

    check_key = get_url(key, db)
    if check_key:
        return {
            'message': 'Такой ключ уже существует! Укажите другой ключ.',
            'category': 'danger',
            'url': url,
            'key': key
        }

    return error
