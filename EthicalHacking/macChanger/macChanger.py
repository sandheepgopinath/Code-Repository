import subprocess
import optparse
import re

parser=optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="Interface")
parser.add_option("-m","--mac",dest="mac",help="New Mac Address")

(options,arguments)=parser.parse_args()

interface=options.interface
mac=options.mac

original_mac=subprocess.check_output(['sudo','ethtool','-P',options.interface])
originalMac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(original_mac))
originalMac=originalMac.group(0)
print('[+] Hardware Mac Address : ' +str(originalMac))

subprocess.call(['sudo','ifconfig',interface,'down'])
subprocess.call(['sudo','ifconfig',interface,'hw','ether',mac])
subprocess.call(['sudo','ifconfig',interface,'up'])
subprocess.call(['sudo','service','network-manager','restart'])
output=subprocess.check_output(['sudo','ifconfig'])


search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output))
if search_result:
	print('[+] New Mac address : '+str(search_result.group(0)))
else:
	print('[+] Unable to change Mac')
