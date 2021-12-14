#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:39:41 2021

@Author : Sandheep Gopinath
@Code :  Stock Price Decision making.

@Details : To decide if we should buy, sell or wait based on the price. 
"""


def createDataset(n):
    from random import randint
    prices=[randint(0,100) for i in range(n) ]
    return prices


def visualise(prices):
    """ The function takes the list of prices as arguments, and creates
    a point plot so that it is easy to visaluise the data and verify the 
    output"""
    
    from seaborn import pointplot
    days=[i for i in range(0,len(prices))]
    pointplot(days,prices)
    
def decide(prices):
    """ This function finds the local minimas and the local maximas. 
    Whenever it finds a local minima, it decides to buy and it is a local maxima,
    it decides to sell. For all the other points, it decides to wait. 
    The idea behind this is to take only the positive increments, and hence
    make only profits
    The function returns the actions dictionary which tells what action was taken at each stage 
    , the total profit acquired by trader and the list of minimas and maximas"""
    
    
    minimas=[] 
    maximas=[]
    lastAction=''
    actionsDictionary={}
    lastMinima=0
    profit=0
    
    for i in range(0,len(prices)):
        try:
            if i==0:
                if prices[i]>prices[i+1]:
                    actionsDictionary[prices[i]]='W'
                else:
                     actionsDictionary[prices[i]]='B'
            elif (prices[i]<prices[i+1]) & ( prices[i]<prices[i-1]):
                minimas.append(prices[i])
                lastAction='B'
                actionsDictionary[prices[i]]='B'
                lastMinima=prices[i]
            elif (prices[i]>prices[i+1]) & ( prices[i]>prices[i-1]):
                maximas.append(prices[i])
                lastAction='S'
                actionsDictionary[prices[i]]='S'
                profit+=(prices[i]-lastMinima)
            else:
                actionsDictionary[prices[i]]='W'
        except:
            if lastAction=='B':
                actionsDictionary[prices[i]]='S'
            else:
                actionsDictionary[prices[i]]='W'
    print('The trader started with ',minimas[0],' rupees and ended up getting a profit of ',profit,'rupees')
    print('\n')
    return actionsDictionary,profit,minimas,maximas

    


l=createDataset(20)
result,profit,minimas, maximas=decide(l)

print('If the trader did only one trade between the smallest minima and largest maxima',end=' ')
print('he could have got a profit of ',max(maximas)-min(minimas))
print('\n')
print('If the trader did only one trade between the first minima and last maxima',end=' ')
print('he could have got a profit of ',maximas[-1]-minimas[0])
print('\n')
print('Buy Sell pattern of the trader',result)

