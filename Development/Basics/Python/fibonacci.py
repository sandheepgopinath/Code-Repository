#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:08:04 2021

@author: Sandheep Gopinath
"""

def fibonacci(n):
    series=[0,1]
    for i in range(n-2):
        newNumber=series[len(series)-1]+series[len(series)-2]
        series.append(newNumber)
    
    return series

n=input('Enter the number of fibonacci series to be displayed: ')
print(fibonacci(int(n)))
        