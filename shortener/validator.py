import validators
import requests


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
