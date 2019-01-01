from hackerman.handlers import bind_base as handler
from hackerman.transport import tcp
from hackerman.crypto import xor

class Handler(handler.BaseHandler):
	def __init__(self, port, password):
		conn = tcp.Server(port)
		crypt = xor.XORCrypt(password)
		super().__init__(conn, crypt)