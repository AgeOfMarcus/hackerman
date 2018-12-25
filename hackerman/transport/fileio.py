from hackerman import utils
import os

class FileIO(object):
	def __init__(self, fn):
		self.fn = fn
		os.system("touch "+fn)
	def send(self, raw):
		enc = utils.b64e(raw)
		tw = enc+":::send"
		while open(self.fn,"r").read().endswith(":::send"):
			pass
		with open(self.fn, "w") as f:
			f.write(tw)
	def recv(self):
		r = open(self.fn, "r").read()
		while not r.endswith(":::send"):
			r = open(self.fn, "r").read()
		m = utils.b64d(r.split(":::send")[0])
		with open(self.fn, "w") as f:
			f.write("recv")
		return m