#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:02:39 2021

@author: Sandheep Gopinath
"""


def ThreeSum(l):
    triplets=[]
    for i in range(len(l)-2):
        for j in range(i,len(l)-1):
            for k in range(j,len(l)-1):
                if i!=j!=k:
                    if l[i]+l[j]+l[k]==0:
                        triplets.append([l[i],l[j],l[k]])
    print(triplets)                    
    
def splitBySpace(string):
    numberList=[]
    previousPointer=0
    for i,n in zip(string,range(len(string))):
        if i==' ':
            number=int(string[previousPointer:n+1])
            previousPointer=n
            numberList.append(number)
    numberList.append(int(string[previousPointer:n+1]))
    return numberList

l=input('Enter the list of numbers ( Seperated by space): ')
ThreeSum(splitBySpace(l))
