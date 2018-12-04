import scapy.all as scapy

class DNS(object):
	def __init__(self, dst="0.0.0.0", sport=0, qname="www.example.com"):
		self.dst = dst
		self.sport = sport
		self.qname = qname
	def pkt(self):
		return scapy.IP(dst=self.dst)/scapy.UDP(sport=self.sport)/scapy.DNS(rd=1, qd=scapy.DNSQR(qname=self.qname))
	def send(self):
		scapy.send(self.pkt())