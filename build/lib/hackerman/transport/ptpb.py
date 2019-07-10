import requests
from hackerman import utils

class ptpb(object):
	def __init__(self, url):
		self.url = url
	def upload(self, raw, uri="/"):
		r = requests.post(self.url+uri, data={'c':raw})
		ln = r.content.decode().strip().split("\n")
		url, uid = ln[-2].split(": ")[1], ln[-1].split(": ")[1]
		return url, uid
	def delete(self, uuid):
		r = requests.delete(self.url+"/"+uuid)
		return r.status_code
	def update(self, raw, uuid):
		r = requests.put(self.url+"/"+uuid,
			data={'c':raw})
		res = r.content.decode().strip().split("\n")
		res = res[5]
		res = res.split(": ")[1]
		return res

class Client(object):
	def __init__(self, secret, url="https://ptpb.pw"):
		self.secret = secret
		self.uri = "/~"+secret
		self.url = url+"/~"+secret
		self.ptpb = ptpb(url)
		self.last = utils.sha256(utils.rand_bytes())
	def send(self, raw):
		while requests.get(self.url).content.decode() == self.last:
			pass
		gt = requests.get(self.url).content
		if not gt.endswith(b'recv'):
			uid = self.ptpb.upload(utils.rand_bytes(),
				uri=self.uri)[1]
		else:
			uid = gt.decode().split(":::")[0]
		ts = utils.b64e(raw)+":::"+uid+":::"+utils.sha256(utils.rand_bytes())
		self.last = ts
		res = self.ptpb.update(ts.encode(),uid)
	def recv(self):
		res = requests.get(self.url).content.decode()
		while res.endswith("recv"):
			res = requests.get(self.url).content.decode()
		dat, uid, ignore = res.split(":::")
		raw = utils.b64d(dat)
		self.ptpb.update(uid.encode()+b':::'+utils.rand_bytes()+b'recv',uid)
		return raw

def maketest():
	return Client(utils.sha256(utils.rand_bytes()))