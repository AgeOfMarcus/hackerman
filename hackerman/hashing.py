import hashlib
from hackerman._hashing.natzil import BadHash as _BH
from cryptography.hazmat.primitives import hashes

r_sha256 = lambda raw: hashlib.sha256(raw)
r_sha1 = lambda raw: hashlib.sha1(raw)
r_md5 = lambda raw: hashlib.md5(raw)
def r_badhash(raw):
    bh = _BH()
    bh.update(raw)
    return bh
def r_sha224(raw):
    digest = hashes.Hash(hashes.SHA224())
    digest.update(raw)
    return digest.finalize()
def r_sha512(raw):
    digest = hashes.Hash(hashes.SHA512())
    digest.update(raw)
    return digest.finalize()
def r_sha3_256(raw):
    digest = hashes.Hash(hashes.SHA3_256())
    digest.update(raw)
    return digest.finalize()


def sha256(raw, hex=True):
    return r_sha256(raw).hexdigest() if hex else r_sha256(raw).digest()
def sha1(raw, hex=True):
    return r_sha1(raw).hexdigest() if hex else r_sha1(raw).digest()
def md5(raw, hex=True):
    return r_md5(raw).hexdigest() if hex else r_md5(raw).digest()
def natzil(raw, hex=True):
    return r_badhash(raw).hexdigest() if hex else bytes.fromhex(r_badhash(raw).hexdigest())
def sha224(raw, hex=True):
    return r_sha224(raw).hex() if hex else r_sha224(raw)
def sha512(raw, hex=True):
    return r_sha512(raw).hex() if hex else r_sha512(raw)
def sha3_256(raw, hex=True):
    return r_sha3_256(raw).hex() if hex else r_sha3_256(raw)