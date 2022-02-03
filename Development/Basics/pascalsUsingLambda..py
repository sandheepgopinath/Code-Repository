#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:26:14 2021

@author: Sandheep Gopinath

Usage of Lambda Functions : The code has been modified by implementing lambda functions in a couple of places. 
It is just to demonstrate the usage of Lambda functions. 
Learning : When lists are passed to Lambda functions, the original lists are getting modified. Call by reference
But when passing integers other data types, it is call by value where the original value passed is not getting modified. 




Code without using Lambda functions


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

"""



appendZero=lambda x: x.append(0) # Lambda function to append a 0 to end of list
appendStartZero=lambda x: x.insert(0,0) # Lambda function to append 0 to end of list
newLayer=lambda emptyList,newList: [emptyList.append(newList[i]+newList[i+1]) for i in range(len(newList)-1)] # Lambda function to create a new layer
printCommand=lambda l: [print(" %3d " %(element),end='   ') for element in l if element!=0] # Lambda function to print each layer
initialize=lambda x : x.append([0,1,0]) # Function to initialise the pascals triangle. 

def pascalsList(numberOfLayers):
        """ Create a list of element for Pascals triangle. 
            This list has to be printed using a pretty print function or else
            it would appear just like a list of lists"""
            
        pTriangle=[]
        initialize(pTriangle)
        for i in range(numberOfLayers):
                emptyList=[]
                appendStartZero(emptyList)
                newLayer(emptyList,pTriangle[i])
                appendZero(emptyList)
                pTriangle.append(emptyList)
        return pTriangle


def printPascals(p):
    for i in p:
        spaces=len(p[len(p)-1])-len(i)
        spacer=''
        
        for s in range(spaces):
            spacer+='   '
        print(spacer,end='')
        printCommand(i)
        print('\n')

printPascals(pascalsList(5))