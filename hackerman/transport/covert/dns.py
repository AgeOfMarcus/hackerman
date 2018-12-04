from hackerman.transport import dns
import scapy.all as scapy

def check_domain(pkt, domain, on_pkt):
	if scapy.DNS in pkt and domain in pkt['DNS Question Record'].qname:
		on_pkt(pkt)

def decrypt(pkt):
	byte = pkt.sport.to_bytes(1, "little")
	return byte

class Server(object):
	pass
class Client(object):
	pass