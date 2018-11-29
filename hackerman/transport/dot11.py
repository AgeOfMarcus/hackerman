from scapy.all import *

broadcast = ':'.join(("ff."*6).split(".")[:-1]) # yeet

class Beacon(object):
	def __init__(self, ssid, cap="ESS+privacy"):
		dot11 = Dot11(type=0, subtype=8, addr1=broadcast,
			addr2=str(RandMAC()), addr3=str(RandMAC()))
		beacon = Dot11Beacon(cap=cap)
		essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
		rsn = Dot11Elt(ID="RSNinfo", info=(
			'\x01\x00'
			'\x00\x0f\xac\x02'
			'\x02\x00'
			'\x00\x0f\xac\x04'
			'\x00\x0f\xac\x02'
			'\x01\x00'
			'\x00\x0f\xac\x02'
			'\x00\x00'))
		self.pkt = RadioTap()/dot11/beacon/essid/rsn
	def send(self, iface, times):
		frames = []
		for i in range(0, times):
			frames.append(self.pkt)
		sendp(frames, iface=iface, inter=0.0100 if len(frames) < 10 else 0, loop=0)
		
