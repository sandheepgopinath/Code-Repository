#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:45:04 2021

@author: blink
"""
#Formatted printing


for i in range(0,2):
    print('Hello','How',end=' ',sep='-')
    
pi=22/7

print('Pi',pi)
print((f'Pi {pi:.2f}'))
print('Pi {0:.2f} {1}'.format(pi,10))
print('Pi %.2f %d' %(pi,10))

