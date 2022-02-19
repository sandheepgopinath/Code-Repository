#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 23:52:33 2021

@author: Sandheep Gopinath
"""

def pascals(n):
    pTriangle=[]
    pTriangle.append([0,1,0])
    
    for i in range(n):
        layer=[]
        layer.append(0)
        lastLayer=pTriangle[len(pTriangle)-1]
        for i in range(len(lastLayer)-1):
            temp=lastLayer[i]+lastLayer[i+1]
            layer.append(temp)
        layer.append(0)
        pTriangle.append(layer)
    
    return pTriangle

def printPascals(p):
    for i in p:
        spaces=len(p[len(p)-1])-len(i)
        spacer=''
        
        for s in range(spaces):
            spacer+='   '
        print(spacer,end='')
        for j in i:
            if j!=0:
                print(" %3d " %(j),end='   ')
        print('\n')
        

n=input('Enter number of layers in triangle needed : ')
printPascals(pascals(int(n)))