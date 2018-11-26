'''
Taken from https://github.com/jeffreysasaki/covertchannel/
Credit where credit is due
Minor edits and updates were made by me

This may or may not work, idk
Needs to be run as root :(
'''

import sys, threading, uuid
import scapy.all as scapy

def send(raw, host):
	for byte in raw:
		pkt = scapy.IP(dst=host)/scapy.TCP(sport=byte, dport=scapy.RandNum(0,65535), flags="E")
		scapy.send(pkt)

def recv(end_var, out_var=''.join(str(uuid.uuid4()).split("-"))):
	if not out_var in globals():
		globals()[out_var] = b''
	def parse(pkt):
		flag = pkt['TCP'].flags
		if flag == 0x40:
			char = pkt['TCP'].sport.to_bytes(1, "little")
			globals()[out_var] += char

	e = threading.Event()
	def _sniff(e):
		a = scapy.sniff(filter="tcp", prn=parse, stop_filter=lambda p: e.is_set())
	t = threading.Thread(target=_sniff, args=(e, ))
	t.start()
	while not globals()['end_var']:
		pass
	e.set()
	return res
