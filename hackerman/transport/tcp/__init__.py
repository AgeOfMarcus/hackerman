import socket

class Server(object):
	def __init__(self, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(("0.0.0.0",port))
		sock.listen(10)
		conn, addr = sock.accept()
		self.conn = conn
	def send(self, raw):
		self.conn.send(raw)
	def recv(self, buff=4096):
		return self.conn.recv(buff)

class Client(object):
	def __init__(self, addr):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((addr[0],addr[1]))
		self.conn = conn
	def send(self, raw):
		self.conn.send(raw)
	def recv(self, buff=4096):
		return self.conn.recv(buff)