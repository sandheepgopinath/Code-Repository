#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 01:53:53 2021

@author: blink
"""

val=int(input('Enter the number to compute the factorial'))


if val<0:
    val=val*-1
temp=val
count=1

while temp>9:
    temp/=10
    count+=1
    
print(count)