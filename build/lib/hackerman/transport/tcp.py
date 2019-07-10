import socket

end_s = 'φԤɯӄ\u05cfʧơࢭ\u0604\u0991ʉਜ਼ણଆ\u03a2٭'.encode() # generated randomly, hopefully wont ever be found irl

class RawServer(object):
	def __init__(self, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(("0.0.0.0",port))
		sock.listen(10)
		conn, addr = sock.accept()
		self.conn = conn
	def send(self, raw):
		self.conn.send(raw)
	def recv(self, buff):
		return self.conn.recv(buff)

class RawClient(object):
	def __init__(self, addr):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((addr[0],addr[1]))
		self.conn = conn
	def send(self, raw):
		self.conn.send(raw)
	def recv(self, buff):
		return self.conn.recv(buff)

class Server(object):
	def __init__(self, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(("0.0.0.0",port))
		sock.listen(10)
		conn, addr = sock.accept()
		self.conn = conn
	def send(self, raw, buff=4096):
		todo = raw
		done = "".encode()
		sent = 0
		while not done == raw:
			ts = todo[sent:sent+buff]
			self.conn.send(ts)
			sent += (sent+buff) - sent
			done += ts
		self.conn.send(end_s)
	def recv(self, buff=4096):
		got = "".encode()
		this = self.conn.recv(buff)
		while not this == end_s:
			if this.endswith(end_s):
				got += this.split(end_s)[0]
				break
			got += this
			this = self.conn.recv(buff)
		return got

class Client(object):
	def __init__(self, addr):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((addr[0],addr[1]))
		self.conn = conn
	def send(self, raw, buff=4096):
		todo = raw
		done = "".encode()
		sent = 0
		while not done == raw:
			ts = todo[sent:sent+buff]
			self.conn.send(ts)
			sent += (sent+buff) - sent
			done += ts
		self.conn.send(end_s)
	def recv(self, buff=4096):
		got = "".encode()
		this = self.conn.recv(buff)
		while not this == end_s:
			if this.endswith(end_s):
				got += this.split(end_s)[0]
				break
			got += this
			this = self.conn.recv(buff)
		return got
