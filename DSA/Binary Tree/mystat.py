import os
import sys
from stat import *
import json

def usage(arg):
    print(f'usage: {arg[0]}: <filename>')
    sys.exit(1)


global mystatd
mystatd=None
def mystat(path):
    global mystatd
    if mystatd == None:
        mystatd={}
        with open('stat.json','rb') as f:
           statjson=json.load(f)
        mystatd=json.loads(statjson)

    st=os.stat_result(mystatd[path])
    return st

def main():
    n = len(sys.argv)
    statd={}
    #print(f'argument list {n} {sys.argv}')
    if n < 2: 
        usage(sys.argv)
    filename=sys.argv[1]
#    st=mystat('kernel-0/arch')
    st=mystat(filename)
    print(st)

if __name__ == "__main__":
    main()
