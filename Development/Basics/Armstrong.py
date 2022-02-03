#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:15:03 2021

@author: Sandheep Gopinath
"""

def reverseList(l):                                                            # Function to reverse the elements in a list
    newList=[]
    for i in range(len(l)-1,-1,-1):
        newList.append(l[i])
    return newList


def findDigits(n):                                                             # Function to find the inidivdual digits and number of digits in a number
    numbers=[]
    number=0
    while(n>0):                                                                # Keeps dividing the number until all numbers are processed
        numbers.append(n%10)
        n=int(n/10)
        number+=1                                                              # Counts the number of digits 
    numbers=reverseList(numbers)
    return(numbers,number)                                                     # Function returns the list of digits and total number of digits




def power(number,power):  
    total=number                                                               # Function to find power of a number
    for i in range(power-1):                                                   # Multiplies the number 'power' times and returns result
        total*=number
    return total

        

def checkArmstrong(n):                                                         # Function to check if a number is Armstrong
    numberList,nDigits=findDigits(n)                                           # Find the individual digits and number of digits
    total=0
    for digit in numberList:
        total+=power(digit,nDigits)                                            # Checks the condition for Armstrong
        # print(digit,n,power(digit,n),total)
    if total==n:
        return True
    else:
        return False
    
    
    
count=0 
number=0
armstrongs=[]
while number<=10000:
    if checkArmstrong(int(number)):
        armstrongs.append(number)
        count+=1   
    else:
        pass
    number+=1

print(armstrongs)


#%%
n=input('Enter number to be checked if Armstrong : ')
if checkArmstrong(int(n)):
    print('Number is Armstrong')
else:
    print('Number is not Armstrong')