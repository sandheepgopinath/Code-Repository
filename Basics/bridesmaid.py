#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:15:33 2021

@author: blink
"""

l=[0,2,1,4,1,0]
l0=[0,2,1,4,5,6]
l1=[2,3,1,0,5]
l2=[0,1,2,3,4,5]
l3=[5,4,3,2,1,0]


def flowers(l):
    flower=[1,1,1,1,1,1]
    for i in range(1,len(l)-1):
        if (l[i]>l[i-1]) & (l[i]>l[i+1]):
            flower[i]+=1
        elif (l[i]>l[i-1]) & (l[i]<l[i+1]):
            if flower[i-1]>flower[i]:
                flower[i]=flower[i-1]
            flower[i]+=1
        elif (l[i]<l[i-1])& (l[i]>l[i+1]):
            if flower[i-1]<flower[i]:
                flower[i]=flower[i-1]
            flower[i]+=1
        elif (l[i]<l[i-1])& (l[i]>l[i+1]):
            pass
        print(flower,i,l[i],'\n')

    return flower

def biggest(a,b):
    if a>b:
        return a
    else:
        return b
    
def process(l):
    flower=[]
    for i in range(len(l)):
        flower.append(0)
    midPoint=int(len(l)/2 if len(l)%2==0 else (len(l)+1)/2)-1
    
    for i in range(2) :
        for i in range(1,len(l)-1):
            if (l[i]>=l[i-1]) & (l[i]>=l[i+1]):
                # print('One')
                temp=biggest(flower[i-1],flower[i+1])+1
                flower[i]=temp
            elif (l[i]<=l[i-1]) & (l[i]<=l[i+1]):
                # print('Two')
                pass
            elif (l[i]<=l[i-1]) & (l[i]>=l[i+1]):
                # print('Three')
                if flower[i]<=flower[i+1]:
                    flower[i]=flower[i+1]+1
                    if flower[i-1]<=flower[i]:
                        flower[i-1]=flower[i-1]+1
                        
            elif (l[i]>=l[i-1]) & (l[i]<=l[i+1]):
                # print('Four')
                if flower[i]<=flower[i-1]:
                    flower[i]=flower[i-1]+1
                if flower[i]>=flower[i+1]:
                    flower[i+1]=flower[i]+1
            # print(flower,l[i-1],l[i],l[i+1])      
        if l[len(l)-1]>l[len(l)-2]:
            flower[len(l)-1]=flower[len(l)-2]+1
        else:
            pass
 
        
    if l[len(l)-1]>l[len(l)-2]:
        flower[len(l)-1]=flower[len(l)-2]+1
    if l[0]>l[1]:
        flower[0]=flower[1]+1
    

    for i in range(len(l)):
        flower[i]=flower[i]+1
    return(flower)


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



stringArray=input('Enter the ratings of bridsmaid (Seperated by spaces')
arr=splitBySpace(stringArray)
flowers=process(arr)
minimumFlowers=0
for i in flowers:
    minimumFlowers+=i
print('Flowers would be distributed as ',flowers)
print('Minimum number of flowers needed : ',minimumFlowers)
 