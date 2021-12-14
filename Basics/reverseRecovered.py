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
    return total

def findDigits(n):                                                             # Function to find the inidivdual digits and number of digits in a number
    numbers=[]
    number=0
    while(n>0):                                                                # Keeps dividing the number until all numbers are processed
        numbers.append(n%10)
        n=int(n/10)
        number+=1   
    reverse=0                                                     # Counts the number of digits 
    for digit in numbers:
        reverse+=(digit*power(10,number))
        number-=1
        print(reverse)
                 
  
findDigits(100)