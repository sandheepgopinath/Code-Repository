#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:39:41 2021

@author: blink
"""

#Markov chain

def showMatrix(mat1):

    for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                print(mat1[i][j],end=' ')
            print('\n')
            
            
         
def matrixmult(mat1,mat2):
    result=[]   
      
    for i in range(0,len(mat1)):
        tempList=[]
        for j in range(0,len(mat2[0])):
            
            temp=0
            for k in range(0,len(mat1[0])):
                temp+=mat1[i][k]*mat2[k][j]
            tempList.append(round(temp,2))
        result.append(tempList)
    
    # print('\n\nResult')
    # for i in range(len(result)):
    #     for j in range(len(result[0])):
    #         print(result[i][j],end=' ')
    #     print('\n')
    return result

from datetime import datetime as dt
import time

Residence=500
Canteen=0
Lecture=0

rProbability=[0.3,0.6,0.1] #Residence, Canteen, Lecture
cProbability=[0.1,0.8,0.1] #Residence, Canteen, Lecture
lProbability=[0.45,0.5,0.05] #Residence, Canteen, Lecture

probabilityArray=[]
probabilityArray.append(rProbability)
probabilityArray.append(cProbability)
probabilityArray.append(lProbability)

distribution=[[500],[0],[0]]


for i in range(0,24):
    distribution=matrixmult(probabilityArray,distribution)
    print(distribution)
    print('---------------------Hour ',i, '---------------------------------\n')
    time.sleep(1)
