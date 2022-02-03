import subprocess,os,re

result=subprocess.Popen(['ps -ax | grep flask'],shell=True,stdout=subprocess.PIPE)
result=str(result.communicate()[0])
id=int(re.findall('(\d*) pts',result)[0])
command='kill -KILL '+str(id)
subprocess.run(['kill','-KILL',str(id)])
