'''
hackerman.transport.covert.dns is a serverless method of covert comms
information is transferred through DNS requests only
the source port of each request is actually the byte of data.

The only downside to this is that it's very slow and the clients need to
be on the same network

Usage:
	client1 = Client() # listen and send can be anything, just swap them around for the other client
	client2 = Client(listen=client1.send_domain, send=client1.listen_domain)
	client1.send("hello world".encode())
	recv = client2.recv()
	print(recv.decode() == "hello world") # check if the data is the same
'''

from hackerman.transport import dns
from hackerman import utils
import scapy.all as scapy

end_s = b'\xf1\xad\xa1\xb4\xf1\x88\x9e\xb1\xf2\x89\x83\xbc\xf1\x98\xbf\xa3'

def check_domain(pkt, domain):
	if type(domain) == str:
		domain = domain.encode()
	if scapy.DNS in pkt and 'DNS Question Record' in pkt and domain in pkt['DNS Question Record'].qname:
		return True

def decrypt(pkt):
	byte = pkt.sport.to_bytes(1, "little")
	return byte

class Client(object):
	def __init__(self, listen="listen.example.com", send="send.example.com"):
		self.listen_domain = listen
		self.send_domain = send
	def on_pkt(self, pkt):
		if check_domain(pkt, self.listen_domain):
			return decrypt(pkt)
		else:
			return b'' # adds none
	def prn(self, pkt):
		self.buf += self.on_pkt(pkt)
	def recv(self):
		self.buf = b''

		while True:
			if len(self.buf) >= len(end_s):
				if self.buf[len(self.buf)-len(end_s):] == end_s:
					break
			scapy.sniff(
					store=0,
					stop_filter=lambda x: scapy.DNS in x,
					prn=self.prn
				)

		buf = self.buf[:len(self.buf)-len(end_s)]
		self.buf = b''
		return buf

	def send(self, raw):
		pkt = dns.DNS(qname=self.send_domain)
		for byte in raw:
			pkt.sport = byte
			pkt.send()
		for byte in end_s:
			pkt.sport = byte
			pkt.send()

class SpeedyClient(object):
	def __init__(self, listen="listen.com", send="send.com"):
		self.listen = listen
		self.send = send
		self.eof = 6969 # nice
		self.buf = b''
	def on_pkt(self, pkt):
		if check_domain(pkt, self.listen):
			return self.decrypt(pkt)
		else:
			return b''
	def decrypt(self, pkt):
		return utils.b64d(pkt['DNS'].qd.qname.decode().split(".")[0])
	def prn(self, pkt):
		self.buf += self.on_pkt(pkt)

	def recv(self):
		self.buf = b''

		while True:
			
		
