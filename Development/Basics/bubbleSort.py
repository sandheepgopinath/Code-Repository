#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:43:38 2021

@author: blink
"""


def bubbleSort(l):                                                             # Function to do bubble sort
    endPointer=len(l)-1                                                                        # Initialising the position of end Pointer for bubble sort. 
    for i in range(endPointer,-1,-1):                                          # For loop to iterate over list. The iteration gets smaller each time
        for j in range(0,i):                                                   # Second for loop to arrange consicutive elements
            if l[j]<=l[j+1]:
                temp=l[j]                                                      # Swap algorithm
                l[j]=l[j+1]
                l[j+1]=temp
    return l


def selectionSort(l):                                                          # Fuction to do selection sort
    for i in range(len(l)-1):                                                  # Iterating from 0th to second last element
        smallest=l[i]                                                          # Assuming that the ith element is the smallest
        flag=0
        for j in range(i+1,len(l)):                                            # For loop to iterate from i+1 th element to last element in the list
            if l[j]<=smallest:                                                 # Check for elements smaller than 'smallest'
                smallest=l[j]
                idx=j
                flag=1
        if flag==1:                                                            # Swaping the smallest element to the ith position
            temp=l[idx]                                                        # Swap algorithm
            l[idx]=l[i]
            l[i]=temp
    return l


def createList(number):                                                        # Function to create a list of n random numbers
    from random import randint
    
    l=[]
    for i in range(number):
        l.append(randint(0,100))
    return l



def linearSearch(l,element):                                                   # Function to do linear search
        position=[]
        for i,pos in zip(l,range(0,len(l))):
            if i==element:
                position.append(pos)
        return position
        


def binarySearch(l,element,isSorted=False):
    found=[]                                    
    if isSorted:
        l=bubbleSort(l)
    midPoint=0
  
    
    if len(l)%2==0:
        midPoint=int(len(l)/2)-1
    else:
        midPoint=int((len(l)+1)/2)-1

    
    if l[midPoint]==element:
        found.append(midPoint)
        
                
    print(midPoint,l,len(l))
    
    while(len(l)>1):   
    
        
        if int(element)<l[midPoint]:
            l=l[0:midPoint]
        else:
            l=l[midPoint:len(l)]
            
            
        if len(l)%2==0:
            midPoint=int(len(l)/2)-1
        else:
            midPoint=int((len(l)+1)/2)-1
            
        if midPoint==0:
            break
        
        
   
        if l[midPoint]==element:
            found.append(midPoint)
            
            
        print(midPoint,l,len(l))
        
def binarySearch1(l,element,isSorted=False):
    def midP(value):
        if value%2==0:
            midPoint=int(value/2)-1
        else:
            midPoint=int((value+1)/2)-1
        return midPoint


    midPoint=0 
    elementPos=[]                                                              # Initializing the variable midpoint
    if isSorted:                                                               # Sorting the array if nor sorted
       l=bubbleSort(l)
    midPoint=midP(len(l))
    
    #start with mid point = half of length

    if l[midPoint]==int(element):                                              # If element is found at midpoint, marking the index to a list
        elementPos.append(midPoint)
        for i in range(midPoint+1,len(l)):                                     # Checking if the same element is present more than one to the right side 
            if l[i]==element:
                elementPos.append(i)
            else:
                break
        for i in range(midPoint-1,0,-1):                                       # Checking if the element is present more than once to the left side
            if l[i]==element:                                                  
                elementPos.append(i)
            else:
                break
         
        print(elementPos)
    elif l[midPoint]<int(element):
        length=midPoint
        midPoint=midP(length)
        
       