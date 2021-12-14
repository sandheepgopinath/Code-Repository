#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:01:57 2021

@author: Sandheep Gopinath
"""

def factorial(number):
    factorial=1
    for i in range(1,number+1):
        factorial*=i
    return factorial
    

n=input('Enter the number to find factorial: ')
print('Factorial of ',n,' is ',factorial(int(n)))