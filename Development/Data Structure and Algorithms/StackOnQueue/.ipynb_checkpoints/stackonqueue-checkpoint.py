import os
import sys
from mylist import *

# mylist is same as that for quiz4 and assignment 3
# mylist is of type queue here it supports enqueue and dequeue methods.
# it is a list of elements where each element object is "myelem" and has 
# next and previous and the object it points to. 
# enqueue(obj) --> adds the object to the end of the list
# dequeue(obj) --> removes the object from the front of the list.
# tail --> points to the end element of the list.
# if que is mylist:
# que.tail -> points to last element of type myelem.
# que.header -> dummy element of type myelem whose object points to itself.
# que.size - > size of the list ie. no of elements.
# first element if list is not empty will be que.header.next
# first object is que.header.obj
# last object is que.tail.obj
# invoke the appropriate enqueue, dequeue methods and the right members
# of the que to implement stack.
#

# leave this function as is

def myqpush(que:mylist, obj):
    
    que.enqueue(obj)
    
    pass

# implement this function

def myqpop(que:mylist):

    if que.size == 0:
        return None

    #In stack the pop happens from the rear end whereas in queue the dequeue happens from the front. 
    # Inorder to implement a stack using queue functions, we can do the dequeue operation N-1 times and then store the dequeuedelements into a new queue
    
    new_queue=mylist('queue')
    for i in range(que.size-1):
        myqpush(new_queue,que.dequeue())
    popped_element=que.dequeue()

    for j in range(new_queue.size):
        myqpush(que,new_queue.dequeue())
                
    return popped_element
    
    
# leave these functions as is

def myqpeek(que:mylist):
    if que.header.next == que.header:
        assert(que.tail == que.header)
        return None
    return que.tail.obj

def myqfirst(que:mylist):
    if que.header.next == que.header:
        return None
    return que.header.next.obj

def myqlast(que:mylist):
    if que.header.next == que.header:
        assert(que.tail == que.header)
        return None
    return que.tail.obj
