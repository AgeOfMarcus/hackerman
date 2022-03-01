def xor(raw: bytes, passwd: str) -> bytes:
    key = passwd.encode()
    if len(key) < len(raw):
        key *= (len(raw) // len(key)) + 1
    return bytes(a ^ b for a, b in zip(raw, key))

encrypt, decrypt = xor, xor # alias

class XORCrypt(object):
    def __init__(self, password):
        self.encrypt = lambda raw: xor(raw, password)
        self.decrypt = lambda raw: xor(raw, password)