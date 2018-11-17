from Crypto.Cipher import Blowfish

def encrypt(raw, password):
	cipher = Blowfish.new(password)
	return cipher.encrypt(raw)

def decrypt(raw, password):
	cipher = Blowfish.new(password)
	return cipher.decrypt(raw)

