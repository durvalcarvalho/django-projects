import hashlib
import random
import string

from django.utils import timezone


def generate_hash():
    chars = string.ascii_letters + string.digits
    selected_chars = random.choices(chars, k=6)
    hash_str = ''.join(selected_chars)
    hash_bytes = hash_str.encode('utf-8')
    hash_obj = hashlib.sha1(hash_bytes)
    return hash_obj.hexdigest()


def date_range(start, end):
    delta = end - start
    dates = []

    for i in range(delta.days + 1):
        dates.append(start + timezone.timedelta(days=i))

    return dates
