from Crypto.PublicKey import RSA
import base64, hashlib

def generate():
	key = RSA.generate(1024)
	priv = key.exportKey("PEM")
	pub = key.publickey().exportKey("PEM")
	onion = base64.b32encode(hashlib.sha1(pub).digest()[:10]).lower().decode()
	return onion+".onion", priv
