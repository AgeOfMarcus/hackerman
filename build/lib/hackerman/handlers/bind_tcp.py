from hackerman.handlers import bind_base as handler
from hackerman.transport import tcp
from hackerman.crypto import xor

class Handler(handler.BaseHandler):
	def __init__(self, addr, password):
		conn = tcp.Client(addr)
		crypt = xor.XORCrypt(password)
		super().__init__(conn, crypt)