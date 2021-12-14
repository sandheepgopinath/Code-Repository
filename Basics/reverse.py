#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:12:14 2021

@author: blink
"""


def reverseList(l):                                                            # Function to reverse the elements in a list
    newList=[]
    for i in range(len(l)-1,-1,-1):
        newList.append(l[i])
        
    return newList


def power(number,power):  
    total=number                                                               # Function to find power of a number
    for i in range(power-1):                                                   # Multiplies the number 'power' times and returns result
        total*=number
    if int(power)==0:
        return 1
    else:
        return total

def reverseDigits(n):                                                          # Function to find the inidivdual digits and number of digits in a number
    numbers=[]
    number=0
    while(n>0):                                                                # Keeps dividing the number until all numbers are processed
        numbers.append(n%10)
        n=int(n/10)
        number+=1   
    number-=1    
    reversedDigit=0                                                            # Counts the number of digits 
    for digit in numbers:
        reversedDigit+=digit*power(10,number)
        number=number-1
    return reversedDigit                                                       # Function returns the list of digits and total number of digits



n=input('Enter the number to be reversed: ')
print('The reversed digit is ',reverseDigits(int(n)))