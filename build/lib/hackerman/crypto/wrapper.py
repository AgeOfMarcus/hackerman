import os, base64

class KeyExchangeError(BaseException):
	pass

def randkey(leng=16):
	return base64.b64encode(os.urandom(leng)).decode()[:leng]

class Server(object):
	def __init__(self, crypt, makecrypt, rand=randkey):
		self.crypt = crypt
		self.makecrypt = makecrypt
		self.rand = rand
	def new_instance(self, conn):
		tmp_key = self.rand()
		tmp_crypt = self.makecrypt(tmp_key)

		conn.send(self.crypt.encrypt(tmp_key.encode()))
		check = conn.recv()
		try:
			ok = tmp_crypt.decrypt(check).decode()
			if not ok == "ok":
				raise KeyExchangeError("Invalid reply / Invalid crypto")
		except Exception as e:
			raise KeyExchangeError("Invalid reply / Invalid crypto / Unable to decrypt, " + str(e))

		return tmp_crypt, tmp_key

class Client(object):
	def __init__(self, crypt, makecrypt):
		self.crypt = crypt
		self.makecrypt = makecrypt
	def new_instance(self, conn):
		try:
			tmp_key = self.crypt.decrypt(conn.recv()).decode()
		except Exception as e:
			raise KeyExchangeError("Cannot recieve key / Decryption Error, "+str(e))
		tmp_crypt = self.makecrypt(tmp_key)
		conn.send(tmp_crypt.encrypt("ok".encode()))

		return tmp_crypt, tmp_key