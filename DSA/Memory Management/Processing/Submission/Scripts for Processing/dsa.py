# Function with constant complexity. 
# This function always does 10 steps irrespective of the input and hence
# Has O(10) complexity. 
import time
global stopTimer
def nComplexity(l):
    """ The function returns the sum of first 10 numbers in a list. 
    """
    global stopTimer
    result=1
    steps=0
    start=time.time()
    execFlag=False
    n=10
    if len(l)<10:
        n=len(l)
    for i in range(n): #Iterating the loop 10 times
        result+=l[i]
        steps+=1
        
        if time.time()-start>stopTimer:
            execFlag=True
            break
            
    if execFlag:
        return result,steps,stopTimer
    else:
        return result,steps,0


#This function has linear complexity. If the input has 10 input, there will be 10 iterations in the function 

def linearComplexity(l,n):
    """ This function requires an array and a search element to be passed and it return if the element is found or not. 
    The complexity of this function and the number of steps taken willl increase linearly with the size of the array"""
    global stopTimer
    import time
    steps=0
    start=time.time()
    flag=False
    execFlag=False
    for num in l:                 # Repeting the process len(l) times
        steps+=1
        if num==n:
            flag=True
        if time.time()-start>stopTimer:
            execFlag=True
            break
            
    if execFlag:
        return flag,steps,stopTimer
    else:
        return flag,steps,0

# This function has nsquared complexity. 
# This function executes two forloops , hence increasing the complexity to n*n


def polynomial(l):                                                            # Function to do bubble sort
    """ The function takes as input a list and sorts it in ascending order. 
    It can be seen that it has two for loops, hence making the complexity n2"""
    global stopTimer
    steps=0
    execTime=0
    start=time.time()
    execFlag=False
    endPointer=len(l)-1                                                        # Initialising the position of end Pointer for bubble sort. 
    for i in range(endPointer,-1,-1):                                          # For loop to iterate over list. The iteration gets smaller each time
        for j in range(0,i):                                                   # Second for loop to arrange consicutive elements
            if l[j]<=l[j+1]:
                temp=l[j]                                                      # Swap algorithm
                l[j]=l[j+1]
                l[j+1]=temp
                steps+=3
            else:
                steps+=1
            if time.time()-start>stopTimer:
                execFlag=True
                break   
    if execFlag:
        return l,steps,stopTimer
    else:
        return l,steps,0

#ncube complexity
def ncube(l):
    """ This function returns all possible combinations with replacement. 
    It contains 3 for loops and hence has ncube complexity. 
    """
    global stopTimer
    start=time.time()
    execFlag=0
    combinations=[]
    steps=0
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            for k in range(j,len(l)):
                combinations.append((l[i],l[j],l[k]))
                steps+=1
                if time.time()-start>stopTimer:
                    execFlag=True
                    break
    
    if execFlag:
        return combinations,steps,stopTimer
    else:
        return combinations,steps,0


# The below function is for binary search, where the array is broken down into 
#half every loop. Hence the complexity of this algorithm becomes log(n)

def logarithmic(l,n):
    """ The function takes as input a list which is sorted in ascending order
    and then keeps diving the list at the midpoint inorder to find the element 
    to be searched 'n'. """
    ### Variables for binary search
    global stopTimer
    midPoint=lambda x:int(x/2) if x%2==0 else int((x+1)/2)   # Lambda function to calculate midpoint
    start=0
    end=len(l)-1
    flag=0
    mid=midPoint(end-start)+start
    found=0
    
    #Variables for monitoring
    steps=0
    execFlag=False
    processStart=time.time()
    
    while mid<end :
        steps+=1
        if l[mid]==n:           # If element found at mid, break the loop
            found=1
            flag=1
            break
        if l[mid]>n:             # If element less than midpoint, Ignore the second half
            end=mid
        else:                    #If element greater than midpoint, Ignore the first half 
            start=mid  
            
        mid=midPoint(end-start)+start # Calling the lambda function to get the midpoint
        if time.time()-processStart>stopTimer:
                execFlag=True
                break
    
    
    if flag==0:                      # Final check to see if element is in start or end
        if l[start]==n or l[end]==n:
            found=1
        else:
            found=0
    if execFlag:
        return found,steps,stopTimer
    else:
        return found,steps,0


# Exponential function.Here, for each value of n, the function will be iterated 2powern times. 
def exponential(n):
    """ The function will return the sum of numbers from 1 to 2**n where n is the value specified by the user
    Eg : If n ==2, output will be 1+2+3+4= 8"""
    global stopTimer
    sum=0
    steps=0
    start=time.time()
    execFlag=False
    for i in range(2**n): # Simple function to iterate the loop 2power n times and each number will be added to sum
        steps+=1
        sum+=i
        if time.time()-start>stopTimer:
            execFlag=True
            break
    if execFlag:
        return sum,steps,stopTimer
    else:
        return sum,steps,0

# This is the main function which will be invoked. 

def Functions(choice):
    """ The function will calculate the time usage,CPU Usage, Memory usage, CPU frequency monitoring etc. 
    The function takes as input the maximum power of 2 and the choice of the function and will return
    a dataframe with the output metrics"""
    global stopTimer
    # Importing libraries
    from subprocess import check_output
    import psutil
    import os
    import re
    import pandas as pd
    import random
    import time
    import numpy as np
    import math
    #%%
    option=''
    numberOfSteps=[]
    timeTaken=[]
    length=[]
    getProcessID=os.getpid()
    print(getProcessID)
    process=psutil.Process(getProcessID) # Reading the memory 
    RSS=[]
    VMS=[]
    core1Freq=[]
    core2Freq=[]
    core3Freq=[]
    core4Freq=[]
    core5Freq=[]
    core6Freq=[]
    core7Freq=[]
    core8Freq=[]
    cpuPct=[]
    Usage=[]
    exitFlag=False
    
    

    #Reading the input file and noting the time taken to read it
    startRead=time.time()
    inputFile=list(np.load('inputwlogs.npy'))
    print('Time taken to read input file: ',time.time()-startRead)

    for i in (pow(2,x) for x in range(1,int(math.log(len(inputFile),2)))):
        l=inputFile[0:i]
        print(i,end=' ')
        #To monitor the Physical and Virtual memory consumed. 
        startRSS=process.memory_info().rss
        startVMS=process.memory_info().vms
        steps=0
        times=0
        # Calling the function
        if choice=='const':
            startTime=time.time()
            result,steps,times=nComplexity(l)
            if times>0:
                exitFlag=True
            else:
                times=time.time()-startTime
            option='O(k) Constant'
        elif choice=='lin':
            startTime=time.time()
            l=[random.randint(0,100) for j in range(i)]
            result,steps,times=linearComplexity(l,100)
            if times>0:
                exitFlag=True
            else:
                times=time.time()-startTime
            option='O(n) Linear'
        elif choice=='quad':
            startTime=time.time()
            l=[random.randint(0,100) for j in range(i)]
            result,steps,times=polynomial(l)
            if times>0:
                exitFlag=True
            else:
                times=time.time()-startTime
            option='O(n2) Quadratic'
        elif choice=='cube':
            startTime=time.time()
            l=[random.randint(0,100) for j in range(i)]
            result,steps,times=ncube(l)
            if times>0:
                exitFlag=True
            else:
                times=time.time()-startTime
            option='O(n3) Cubic'
        elif choice=='log':
            startTime=time.time()
            l=[random.randint(0,100000) for j in range(i)]
            result,steps,times=logarithmic(l,random.randint(0,10000))
            if times>0:
                exitFlag=True
            else:
                times=time.time()-startTime
            option='O(log(n)) Logarithmic'
        elif choice=='exp':
            startTime=time.time()
            result,steps,times=exponential(i)
            if times>0:
                exitFlag=True
            else:
                times=time.time()-startTime
            option='O(2^n) Exponential'
        numberOfSteps.append(steps)

        # CPU Usage
        cpuPct.append(float(re.findall("\d.\d",str(check_output(['ps','-p',str(getProcessID),'-o','%cpu'])))[0]))
        timeTaken.append(times)
        length.append(i)
        RSS.append(((process.memory_info().rss-startRSS)*0.008)/(1024*1024))
        VMS.append(((process.memory_info().vms-startVMS)*0.008)/(1024*1024)) 
        core1Freq.append(psutil.cpu_freq(1)[0].current)
        core2Freq.append(psutil.cpu_freq(1)[1].current)
        core3Freq.append(psutil.cpu_freq(1)[2].current)
        core4Freq.append(psutil.cpu_freq(1)[3].current)
        core5Freq.append(psutil.cpu_freq(1)[4].current)
        core6Freq.append(psutil.cpu_freq(1)[5].current)
        core7Freq.append(psutil.cpu_freq(1)[6].current)
        core8Freq.append(psutil.cpu_freq(1)[7].current)
        del l
        if exitFlag:
            break
    del inputFile   
    df=pd.DataFrame()
    df['Complexity']=[option for i in range(len(length))]
    df['Length']=length
    df['Steps taken']=numberOfSteps
    df['Time Taken']=timeTaken
    df['RSS(in GB)']=RSS
    df['VMS(in GB)']=VMS
    df['Core 1 Frequency']=core1Freq
    df['Core 2 Frequency']=core2Freq
    df['Core 3 Frequency']=core3Freq
    df['Core 4 Frequency']=core4Freq
    df['Core 5 Frequency']=core5Freq
    df['Core 6 Frequency']=core6Freq
    df['Core 7 Frequency']=core7Freq
    df['Core 8 Frequency']=core8Freq
    df['CPU Percentage Used']=cpuPct
    filename=str(option)+'.csv'
    df.to_csv(filename)
    return df
  
    
    
## Main part of code

    
import optparse

parser=optparse.OptionParser()

parser.add_option('-o','--option',dest='option',help='const-Constant, lin- Linear, quad- Quadratic, cube- Cubic,log- Logarithmic, exp- Exponential')
parser.add_option('-t','--timeout',dest='timeout',help='The function timesout and breaks after t seconds')
(options,arguments)=parser.parse_args()


op=options.option
try:
    t=int(options.timeout)
    stopTimer=t
except:
    print('Default timeout of 240 seconds')
    stopTimer=240

import pandas as pd
pd.set_option('display.max_columns', 500)
df=Functions(op)	
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

