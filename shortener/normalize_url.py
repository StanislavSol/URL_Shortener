from urllib.parse import unquote


ADDRESS_INDEX = 4


def normalize_url(url):
    url_parse = unquote(unquote(url[ADDRESS_INDEX:]))
    return url_parse
