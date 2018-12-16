'''
This can only send small chunks of data and each secret
can only be used once.
'''

from hackerman.transport import ptpb as tport
from hackerman import utils

class ptpb(object):
	def __init__(self, secret, url="https://ptpb.pw"):
		self.url = url
		self.secret = secret
	def send(self, raw):
		url = self.url+"~"+utils.b64e(raw)
		data = self.secret
		srv = tport.ptpb(self.url)
		r = srv.upload(data, uri=url)
		if r[0] == "already exists":
			raise BaseException("Secret has been used before")
		else:
			return r[1]
	def recv(self):
		srv = tport.ptpb(self.url)
		r = srv.upload(self.secret)
		if not r[0] == "already exists":
			return None
		enc = r[1].split("~")[1]
		return utils.b64d(enc)