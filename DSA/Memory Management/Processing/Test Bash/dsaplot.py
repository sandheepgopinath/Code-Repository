
def plot(df):
    """ The function will take as input a Pandas dataframe with all metrics and will plot 5 different plots 
    Space Complexity 
    Time Complexity
    CPU Usage
    No of steps
    CPU Frequency. 
    After displaying the graphs the function will also save a copy of the graphs as a PNG File. """
    
    import matplotlib.pyplot as plt
    plt.figure(figsize=(20,10))
    # Plotting Space complexity
    plt.subplot(3,2,1)
    plt.ylim(0,int(df['VMS(in GB)'].max())+10)
    plt.title('Space Complexity with higher order of numbers')
    plt.plot(df['Length'],df['VMS(in GB)'],marker='*')
    plt.plot(df['Length'],df['RSS(in GB)'],marker='*')
    #Plotting time complexity
    plt.subplot(3,2,2)
    plt.ylim(0,int(df['Time Taken'].max())+5)
    plt.title('Time Complexity with higher order of numbers')
    plt.plot(df['Length'],df['Time Taken'],marker='*')

    #CPU Usage 
    plt.subplot(3,2,3)
    plt.ylim(0,int(df['CPU Percentage Used'].max())+5)
    plt.title('CPU Usage with higher order of numbers')
    plt.plot(df['Length'],df['CPU Percentage Used'],marker='*')

    #Steps taken to execute 
    plt.subplot(3,2,4)
    plt.ylim(0,int(df['Steps taken'].max())+5000)
    plt.title('No of steps taken with higher order of numbers')
    plt.plot(df['Length'],df['Steps taken'],marker='*')

    #CPU Frequency
    l=[df['Core 1 Frequency'].max(),df['Core 2 Frequency'].max(),df['Core 3 Frequency'].max(),df['Core 4 Frequency'].max(),df['Core 5 Frequency'].max(),df['Core 6 Frequency'].max(),df['Core 7 Frequency'].max(),df['Core 8 Frequency'].max()]
    
    plt.subplot(3,2,5)
    plt.ylim(0,int(max(l))+1000)
    plt.title('CPU Frequency with higher order of numbers')
    plt.plot(df['Length'],df['Core 1 Frequency'],label='Core1',marker='*')
    plt.plot(df['Length'],df['Core 2 Frequency'],label='Core2',marker='*')
    plt.plot(df['Length'],df['Core 3 Frequency'],label='Core3',marker='*')
    plt.plot(df['Length'],df['Core 4 Frequency'],label='Core4',marker='*')
    plt.plot(df['Length'],df['Core 5 Frequency'],label='Core5',marker='*')
    plt.plot(df['Length'],df['Core 6 Frequency'],label='Core6',marker='*')
    plt.plot(df['Length'],df['Core 7 Frequency'],label='Core7',marker='*')
    plt.plot(df['Length'],df['Core 8 Frequency'],label='Core8',marker='*')
    plt.legend()
    name=df['Complexity'][0]+'.jpg'
    plt.savefig(name)
  

import os
import pandas as pd
for file in os.listdir():
    try:
        if file.split('.')[1]=='csv':
            df=pd.read_csv(file)
            plot(df)
    except:
        pass
         # This will exclude files like __pycache__
