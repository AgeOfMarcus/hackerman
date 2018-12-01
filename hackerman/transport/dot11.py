import scapy.all as scapy

broadcast = ':'.join(("ff."*6).split(".")[:-1]) # yeet

class Beacon(object):
	def __init__(self, ssid, cap="ESS+privacy"):
		dot11 = scapy.Dot11(type=0, subtype=8, addr1=broadcast,
			addr2=str(scapy.RandMAC()), addr3=str(scapy.RandMAC()))
		beacon = scapy.Dot11Beacon(cap=cap)
		essid = scapy.Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
		rsn = scapy.Dot11Elt(ID="RSNinfo", info=(
			'\x01\x00'
			'\x00\x0f\xac\x02'
			'\x02\x00'
			'\x00\x0f\xac\x04'
			'\x00\x0f\xac\x02'
			'\x01\x00'
			'\x00\x0f\xac\x02'
			'\x00\x00'))
		self.pkt = scapy.RadioTap()/dot11/beacon/essid/rsn
	def send(self, iface, times, loop=0):
		frames = []
		for i in range(0, times):
			frames.append(self.pkt)
		scapy.sendp(frames, iface=iface, inter=0.0100 if len(frames) < 10 else 0, loop=loop)
		