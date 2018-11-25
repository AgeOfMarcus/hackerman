from random import getrandbits
from ipaddress import IPv4Address, IPv6Address
from Crypto.PublicKey import RSA
import socket, os, base64, hashlib

def rand_onion():
	key = RSA.generate(1024)
	pub = key.publickey().exportKey("PEM")
	onion = base64.b32encode(hashlib.sha1(pub).digest()[:10]).lower().decode()
	return onion+".onion"

def rand_ipv4():
	bits = getrandbits(32) # integer with 32 random bits
	addr = IPv4Address(bits) # IPv4Address object
	addr_str = str(addr)
	return addr_str
def rand_ipv6():
	bits = getrandbits(128)
	addr = IPv6Address(bits)
	addr_str = addr.compressed
	return addr_str

def knock(ip,port, timeout=0.5):
	c = socket.socket()
	c.settimeout(timeout)
	try:
		c.connect((ip,port))
		c.close()
		return True
	except:
		return False
