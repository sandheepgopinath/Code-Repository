import numpy as np
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

l=[]
for i in range(0,n):
    print(i)
    del l
    l=np.random.randint(0,2**i,2**i)
import os
print(os.getcwd())
np.save('input_woLogs',l)

