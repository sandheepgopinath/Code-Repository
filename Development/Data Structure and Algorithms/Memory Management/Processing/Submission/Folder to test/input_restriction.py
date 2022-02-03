import numpy as np
import os
import psutil
import pandas as pd
import re
from subprocess import check_output
import optparse

parser=optparse.OptionParser()

parser.add_option('-n','--number',dest='number',help='This number is the power of 2, which is used to determine the number of elements in the list. Eg : If n==2, 2^2, 4 elements would be there in list')

(options, arguments)=parser.parse_args()

if options.number==None:
    n=26
else:
    n=int(options.number)

print('Started')
idx=os.getpid()
print(idx)
process=psutil.Process(os.getpid()) # Getting the VMS, RSS and CPU Freq details from PSUTIL
RSS=[]
VMS=[]
totalMemory=[]
coreNumber=[]
cpuPct=[]
#availableRam=[]
rss=0
vms=0
memory=[]
l=[]
for i in range(0,n):
    del l
    print('Started')
    print(i,end=' ')
    coreNumber.append(process.cpu_num())
    cpuPct.append(float(re.findall("\d.\d",str(check_output(['ps','-p',str(idx),'-o','%cpu'])))[0]))
    memory.append(float(re.findall("\d.\d",str(check_output(['ps','-p',str(idx),'-o','%mem'])))[0]))
 #   availableRam.append(round((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total),2))
    rssStart=process.memory_info().rss
    vmsStart=process.memory_info().vms
    l=np.random.randint(0,2**i,2**i)
    RSS.append(((process.memory_info().rss-rssStart)*0.008)/(1024*1024))
    VMS.append(((process.memory_info().vms-vmsStart)*0.008)/(1024*1024))
    totalMemory.append((process.memory_info().rss-rssStart)+(process.memory_info().vms-vmsStart))

inputRestrictions=pd.DataFrame()
inputRestrictions['I Value']=[i for i in range(0,n)]
inputRestrictions['Core Number']=coreNumber
inputRestrictions['CPU Percentage']=cpuPct
#inputRestrictions['Available RAM']=availableRam
inputRestrictions['RSS in GB']=RSS
inputRestrictions['VMS in GB']=VMS
inputRestrictions['Memory']=memory
inputRestrictions['Total Memory Consumed']=inputRestrictions['RSS in GB']+inputRestrictions['VMS in GB']
inputRestrictions.to_csv('inputProcess.csv')
np.save('inputwlogs',l)
