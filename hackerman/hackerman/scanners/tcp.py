from random import getrandbits
from ipaddress import IPv4Address, IPv6Address
import socket

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
