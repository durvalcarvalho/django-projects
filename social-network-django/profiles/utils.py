import uuid

def get_random_code():
    return str(uuid.uuid4()).replace('-', '').lower()[:8]