from Crypto.PublicKey import RSA
import os

class Key(object):
	def __init__(self, imp=False):
		if imp:
			self.key = imp
		else:
			self.key = RSA.generate(4096, os.urandom)
	def encrypt(self, raw):
		enc = self.key.publickey().encrypt(raw, 1024)[0]
		return enc
	def decrypt(self, raw):
		dec = self.key.decrypt(raw)
		return dec
	def export(self, fn):
		with open(fn,"wb") as f:
			f.write(self.key.exportKey())

def importKey(fn):
	dat = open(fn,"r").read()
	key = RSA.importKey(dat)
	return Key(imp=key)