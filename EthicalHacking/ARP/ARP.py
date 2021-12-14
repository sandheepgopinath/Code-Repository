#! /usr/bin/env python3

import scapy.all as scapy
import subprocess
import optparse
import re

def scan(ip):
	#Create an ARP Request packet to broadcast IP
	arp_request=scapy.ARP(pdst=ip)
	#Create an Ethernet Packet to broadast MAC
	ethernet_packet=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	#Append both packets
	arp_broadcast=ethernet_packet/arp_request
	#Send packets SendReceivePacket-srp
	#Returns answered and unanswered list
	answered,unanswered=scapy.srp(arp_broadcast,timeout=1,verbose=False)
#	print (answered.summary())	
	for device in answered:
		print(device[1].psrc,'  ',device[1].hwsrc,'\n')

	

parser=optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface")

options,arguments=parser.parse_args()

mac=subprocess.check_output(['sudo','ethtool','-P',options.interface])
mac=re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',str(mac))
print('Hardware Mac: ',mac.group(0),'\n')
print('\t IP \t\t MAC')
print('--------------------------------------')
scan('192.168.1.1/24')
