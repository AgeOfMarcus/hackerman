from Crypto.Cipher import XOR

def encrypt(raw, passwd):
	cipher = XOR.new(passwd)
	enc = cipher.encrypt(raw)
	return enc
def decrypt(raw, passwd):
	cipher = XOR.new(passwd)
	dec = cipher.decrypt(raw)
	return dec