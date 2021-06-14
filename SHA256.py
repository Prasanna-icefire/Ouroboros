import hashlib
def SHA(string):
    encoded=string.encode()
    result = hashlib.sha256(encoded)
    return(result.hexdigest())
