import string
import secrets
from shortener_app.crud import get_url


def get_random_key(db):
    chars = string.ascii_letters + string.digits
    key = "".join(secrets.choice(chars) for _ in range(5))
    return key


def create_unique_random_key(db):
    key = get_random_key(db)
    while get_url(key, db):
        key = get_random_key(db)
    return key
