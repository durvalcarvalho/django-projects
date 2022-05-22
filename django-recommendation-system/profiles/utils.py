import uuid

def generate_ref_code():
    return uuid.uuid4().hex[:12].upper()
