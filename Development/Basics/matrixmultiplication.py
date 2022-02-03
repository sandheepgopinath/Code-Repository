#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:47:28 2021

@author: blink
"""

#Matrix Multiplication

mat1=[[1,2,3],[1,2,3],[1,2,3]]
mat2=[[1,2,5],[4,5,5],[4,5,5]]
result=[]
#Printing matrices
print('Matrix 1')
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        print(mat1[i][j],end=' ')
    print('\n')
    
print('Matrix 2')
for i in range(len(mat2)):
    for j in range(len(mat2[0])):
        print(mat2[i][j],end=' ')
    print('\n')
    
for i in range(0,len(mat1)):
    tempList=[]
    for j in range(0,len(mat2[0])):
        
        temp=0
        for k in range(0,len(mat1[0])):
            temp+=mat1[i][k]*mat2[k][j]
        tempList.append(temp)
    result.append(tempList)

print('\n\nResult')
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end=' ')
    print('\n')
    