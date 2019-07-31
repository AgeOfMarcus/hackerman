import hashlib
from hackerman._hashing.natzil import BadHash as _BH

r_sha256 = lambda raw: hashlib.sha256(raw)
r_sha1 = lambda raw: hashlib.sha1(raw)
r_md5 = lambda raw: hashlib.md5(raw)
def r_badhash(raw):
	bh = _BH()
	bh.update(raw)
	return bh

def sha256(raw, hex=True):
	return r_sha256(raw).hexdigest() if hex else r_sha256(raw).digest()
def sha1(raw, hex=True):
	return r_sha1(raw).hexdigest() if hex else r_sha1(raw).digest()
def md5(raw, hex=True):
	return r_md5(raw).hexdigest() if hex else r_md5(raw).digest()
def natzil(raw):
	return r_badhash(raw).hexdigest()
