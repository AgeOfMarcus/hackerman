import scapy.all as scapy
from hackerman import utils
'''
Client to Client covert channel over malformed dot11 beacons
'''

broadcast = "ff:ff:ff:ff:ff:ff"

class Client(object):
	def __init__(self, channel="covert", iface="wlan0", sender=str(scapy.RandMAC())):
		self.channel = channel
		self.ssid = ssid
		self.iface = iface
		self.sender = sender
		self.buf = b''
	def pkt(self, info):
		dot11 = scapy.Dot11(
				type=0,
				subtype=8,
				addr1=broadcast,
				addr2=self.sender,
				addr3=self.sender
			)
		beacon = Dot11Beacon()
		essid = Dot11Elt(
				ID=self.channel,
				info=info,
				len=len(info)
			)
		frame = scapy.RadioTap()/dot11/beacon/essid
		return frame
	def send(self, inter=0.1, loop=0):
		scapy.sendp(self.pkt(), iface=self.iface, inter=inter, loop=loop)

	def recv(self):
		self.buf = b''
		while not self.stop:
			scapy.sniff(iface=self.iface, prn=self.prn,
				stop_filter=lambda x: scapy.Dot11 in x,
				store=0)
		recv = self.buf
	def prn(self, pkt):
		if pkt.haslayer(scapy.Dot11Elt):
			if not pkt['Dot11Elt'] #CONT
