#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:51:25 2021

@author: Sandheep Gopinath
@Function: To find the Kth largest element 
"""

def splitList(listToSplit,pivot):
    
    """ This function will split a given list into three parts. 
        The first part would be having elements less than or equal to the pivot
        The middle part would be the pivot
        The right part would be having the elements greater than the pivot
    """
    leftList=[]
    rightList=[]
    for position in range(1,len(listToSplit)):
        if listToSplit[position]<=pivot:
            leftList.append(listToSplit[position])
        else:
            rightList.append(listToSplit[position])
    return leftList,[pivot],rightList


def kthLargest(l,k):
    """ This function will keep slitting the list into smaller and smaller lists
    until the kth largest element is found in the pivot. 
    The function will also return the number of iterations it took to 
    find the Kth largest element. 
    """
    position=k
    pivot=l[0]
    left,pivot,right=splitList(l,pivot)
    numberOfSteps=0
    while(1):
        numberOfSteps+=1
        if (len(right)+1==k):
            print('\nThe ',position,'th largest number is ',pivot[0])
            break
        if len(right)>=k:
            left,pivot,right=splitList(right, right[0])
            
        elif len(right)<k:
            if len(right)+1<k:
                k-=(len(right)+1)
                left,pivot,right=splitList(left,left[0])
    
        elif len(left)<k:
            if len(left)+1<k:
                left,pivot,right=splitList(right, pivot)
                
    print('Operation completed in ',numberOfSteps,' iterations')
    
l=input('Enter the elements of list ( Seperated by space)')
l=l.split(' ')
l=[int(element) for element in l]
k=input('Enter the number of the largest element to be found (Eg : 1 for 1st largest element)')
k=int(k)

kthLargest(l, k)