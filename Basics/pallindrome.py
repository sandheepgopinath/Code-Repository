#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:31:29 2021

@author: Sandheep Gopinath
@Program : To check if a string is pallindrome or not

"""
def pallindrome(string):
    """ Function to check if a given number is pallindrome or not
        Here there are two pointers which starts from either side
        of the list. It will continue moving until it reaches the center
        of the list. If the elements are not matching in any iterations, 
        it rbeaks out of the loop, meaning that it is not a pallindrome"""
    string=string.lower()
    half=lambda x: int(x/2) if x%2==0 else int((x+1)/2)                        # Lambda function to find half of a number
    length=half(len(string))
    flag=0                                                                 
    for i,j in zip(range(0,length+1),range(len(string)-1,length-1,-1)):        # Iterating from start to mid and end to mid simaltaneously. 
        if string[i]!=string[j]:                                               # If any of the last end starting letters doesnt match break from loop
            flag=1                                                             # Else repeat the loop until the entire string is checked
            break
    if flag==0:
        return 1
    else:
        return 0                                                               # Return 1 if pallindrome, else 0

string='<MalayalAm<'
if pallindrome(string)==1:
    print(string,' is a pallindrome')
else:
    print(string,' is not a pallindrome')

