#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 08:25:58 2021

@author: Sandheep Gopinath
@program: Program to simlate movement in 2D space
"""
#Declaring 4 lambda functions for movement in each of 4 directions. 
#Diagonal movements are not considered in this case.

moveLeft =lambda x,y: [x-1,y]
moveRight=lambda x,y: [x+1,y]
moveUp=lambda x,y:[x,y+1]
moveDown=lambda x,y:[x,y-1]


def moveN(start,n,listToAppend,direction):
    """ Function to move in either of the four directions by any number
        start: a list of length 2 with starting cordinates
        n : Number of steps to be moved
        listToAppend : the list with all cordinates through which movement happens
        direction ={'l': to move to left,'u': to move up,'d': to move down,'r': to move right}
        """
    for i in range(n):
        if direction=='l':
            nextPosition=moveLeft(start[0],start[1])
        elif direction=='r':
            nextPosition=moveRight(start[0],start[1])
        elif direction=='u':
            nextPosition=moveUp(start[0],start[1])
        elif direction=='d':
            nextPosition=moveDown(start[0],start[1])
        listToAppend.append(nextPosition)

        start=nextPosition
    endPosition=start
    return listToAppend,endPosition

def createMovementList(number):
    """ Function to create the movement path ( corindates) for a number step movement. 
         Upon inspection, it can the seen the the steps changes like below for each rectangle
         down : 2,4,6,8,10,12
         left : 3,5,7,9,11,13
         up   : 3,5,7,9,11,13
         right : 4,6,8,10,12
         
         ie, for the second rectangle, it would be 2 steps down, 3 left , 3 up and 4 right
         It can be generalised that if number of steps down=i
         steps to left = i+1
         steps to top = i+1
         steps to right = i+2
         
         This format is used in for loop to create the cordinate list
    """
    
         
    movementList=[]
    # Define the starting position
    startingPosition=[0,0]
    movementList.append([startingPosition[0],startingPosition[1]])               # Appending the starting position to list
    i=1                                                                          #Creating the first spiral as from second onwards it follows a sequence
    movementList,startingPosition=moveN(startingPosition,i,movementList,'r')
    movementList,startingPosition=moveN(startingPosition,i,movementList,'u')
    movementList,startingPosition=moveN(startingPosition,i+1,movementList,'l')
    i=2
    while(len(movementList)<=number):                                                # Creating more spirals by moving in rectangles, the number of steps increasing each time
        movementList,startingPosition=moveN(startingPosition,i,movementList,'d')     #Break out of the loop when there are 'number' items in the list
        movementList,startingPosition=moveN(startingPosition,i+1,movementList,'r')  
        movementList,startingPosition=moveN(startingPosition,i+1,movementList,'u')
        movementList,startingPosition=moveN(startingPosition,i+2,movementList,'l')
        i+=2
    
    movementList=movementList[0:number]                                         # There can still be a few extra elements as the iteration adds a few elements each time. 
    return movementList                                                         # Hence slicing the list before returning 


print('For n=4 \n')
print(createMovementList(4))

print('\n\nFor n=11 \n')
print(createMovementList(11))