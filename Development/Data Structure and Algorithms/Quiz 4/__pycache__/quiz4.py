
from mylist import *


#
#  the mylist object is initialized as follows.
#
#class myelem():
#    def __init__(self, obj):
#        self.next=self
#        self.prev=self
#        self.obj=obj
#
#class mylist():
#    list_type=['stack', 'list', 'queue']
#
#    # init function do not change this.
#
#    def __init__(self, type):
#        self.header=myelem(self)
#        self.size=0
#        if type not in self.list_type:
#            raise Exception("List type incorrect")
#        self.type=type
#        self.tail=myl.header

# write the code to implement the following functions
# that correspond to mylist ADT but writteen one op at
# time here for testing purpose.
# assume that myl (mylist object) is initialized for the
# right queue type for appropriate function call.
# you can access members of mylist object listed above in 
# the __init__ function for mylist..


# NOTE: update all the members relevant for the operations below.
# like tail, size, etc.,


# Add the object to the list increment the size.

def myadd(myl: mylist, obj):
    if myl.type != 'list':
            raise Exception("Add op supported only for list")
    else:
        node=myelem(obj)
        node.obj=obj
        node.prev=myl.header
        node.next=myl.header.next
        myl.header.next=node
        if myl.size==0:
            myl.tail=node
            myl.header.prev=myl.tail
            myl.size+=1
        else:
            myl.header.next.prev=node
            myl.size+=1


# Enqueue the object as per the queue definition

def myenqueue(myl: mylist, obj):
    if myl.type != 'queue':
        raise Exception("Enqueue op supported only for queue")
    else:
        node=myelem(obj)
        node.obj=obj
        node.next=myl.header
        if myl.size==0:
            node.prev=myl.header
            myl.header.next=node
            myl.tail=node
            myl.header.prev=myl.tail
            myl.size+=1
        else:
            node.prev=myl.tail
            myl.tail.next=node
            myl.tail=node
            myl.size+=1


# Push the object on the stack as per the definition

def mypush(myl: mylist, obj):
    if myl.type != 'stack':
        raise Exception("push op supported only for stack")
    else:
        node=myelem(obj)
        node.obj=obj
        node.next=myl.header
        if myl.size==0:
            node.prev=myl.header
            myl.header.next=node
            myl.tail=node
            myl.header.prev=myl.tail
            myl.size+=1
        else:
            node.prev=myl.tail
            myl.tail.next=node
            myl.tail=node
            myl.size+=1


# Delete the object from the list, be it a list, stack or queue

def mydelete(myl: mylist, obj):
    foundFlag=0
    iterObject=myl.header.next
    while iterObject!=myl.header:
        if iterObject.obj==obj:
            previous=iterObject.prev
            nex=iterObject.next
            previous.next=iterObject.next
            nex.prev=iterObject.prev
            if iterObject==myl.tail:
                myl.tail=myl.tail.prev
            myl.size-=1
            
            break 
        iterObject=iterObject.next
    
            

# mylookup returns the object if object is found else, None.
# cmp function is sent some time for users of
# the lookup to return the right object. Use it to compare
# the equality of the object.

def mylookup(myl: mylist, val, cmp=None):
    foundFlag=0
    myl.iter=myl.header.next
    while myl.iter!=myl.header:
        if myl.iter.obj==val:
            return val
            break
        myl.iter=myl.iter.next

# pop the stack element as per the definition
# return object

def mypop(myl: mylist):
    if myl.type != 'stack':
        raise Exception("pop op supported only for stack")
    else:
        if myl.header!=myl.tail:
            if myl.size>1:
                poppedValue=myl.header.next.obj
                myl.header.next.next.prev=myl.header
                myl.header.next=myl.header.next.next
            else:
                poppedValue=myl.header.next.obj
                myl.header.next=myl.header
                myl.header.prev=myl.header
                myl.tail=myl.header
            myl.size-=1
            return poppedValue
# give the peek value of the stack as per definition
# return object

def mypeek(myl: mylist):
    if myl.type != 'stack':
            raise Exception("peek op supported only for stack")
    else:
        return myl.header.next.obj

# dequeue the object from the list as per the definition

def mydequeue(myl: mylist):
    if myl.type != 'queue':
        raise Exception("Dequeue op supported only for queue")
    else:
        if myl.header!=myl.tail:
            if myl.size>1:
                dequeued=myl.header.next.obj
                myl.header.next=myl.header.next.next
                myl.header.next.next.prev=myl.header
            else:
                dequeued=myl.header.next.obj
                myl.header.next=myl.header
                myl.header.prev=myl.header
                myl.tail=myl.header
            myl.size-=1
            return dequeued

# write the code to delete all the elements passed in 
# myl object.

def mydeleteall(myl:mylist):
    myl.header=myelem(myl)
    myl.size=0
    myl.tail=myl.header


