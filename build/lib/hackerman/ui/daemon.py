import socket

class Daemon(object):
	def __init__(self, port):
		self.port = port
	def listen(self, on_msg, log=lambda x: print("[DEBUG]",x), err=lambda x: print("[ERROR]",x)):
		while True:
			try:
				s = socket.socket()
				s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				s.bind(("127.0.0.1",self.port))
				s.listen(10)

				conn, addr = s.accept()
				log("Connection from [%s]" % str(addr))

				msg = conn.recv(4096)
				log("Msg recieved (%i bytes)" % len(msg))

				on_msg(msg, conn)
				conn.close()
			except Exception as e:
				err(e)

def test():
	d = Daemon(1337)
	d.listen(lambda msg, conn: conn.send("echo: ".encode()+msg))