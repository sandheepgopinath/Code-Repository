# -*- coding: utf-8 -*-
"""
Spyder Editor
@Author: sandheep Gopinath
@Program : To find a sub string within a string without inbuilt functions

"""


def search(givenString,searchString):
    """ Function to search for a sub string within a string. 
        The first letter of the substring is searched within the 
        original string.One the first letter is found, then the remanining letters are checked 
        in a loop equal to the size of the length of the search string"""
    
    lowerVersion=givenString.lower()                                           #Converting the stringto lowercase to search irresepctive of case
    searchString=searchString.lower()                                          # Converting to lowercase to make it non case sensitive
    position=0
    searchLength=len(searchString)
    flag=1
    for i in range(0,len(lowerVersion)):                                       # Loop to find the first letter of seach String in main String
        
        if lowerVersion[i]==searchString[0]:                                   # If first letter matches, check the remaining letters. 
            
            flag=0
            for j,k in zip(range(i,i+len(searchString)),range(0,len(searchString))): 
                try:
                    if lowerVersion[j]!=searchString[k]:
                        flag=1
                except:
                    flag=1
            if flag==0:
                position=i
                break
    
    if flag==0:
        return position
    else:
        return None                                                            # Return the position of  word in string if found. Else return None


string='Hello How are you?'
searchElement='How'

print("'",searchElement,"' found at ",search(string,searchElement),"th position in string")