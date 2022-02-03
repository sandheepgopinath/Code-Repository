import os
import sys

# as discussed in the class and subsequent discussions 
# have an ADT for this and you can use this to create
# whatever you want.
# you are welcome to implement this in a way you want and use it.
# I am giving you a template where a single linked list
# can be used for multiple objects .. 
# to share code as much as possible in a single ADT.
# l1 = selfist(list) --> behaves like a list
# l2 = mylist(stack) --> supports stack and other operations(like push, pop
# etc.)  are disallowed.
# l3 = mylist(queue) --> same here. (like enqueue, dequeue etc.)

# you are welcome to use your own ADT whatever way.
# The function takes as input the server or the vm class object.And creates a node accordingly. 
class myelem():
    def __init__(self,obj):
        self.next=self
        self.prev=self
        self.obj=obj
    def __str__(self):
        return obj    
class mylist():
    list_type=['stack', 'list', 'queue']

    # init function do not change this.

    def __init__(self, type):
        self.header=myelem(self)
        self.size=0
        if type not in self.list_type:
            raise Exception("List type incorrect")
        self.type=type
        self.tail=self.header

    # cmp function is sent some time for users of
    # the lookup to return the right object. See usage
    # below. See same_
    # see comment in mycrm.py above server_same and vm_same.. functions.
    # the cmp method is used if it is not None to check for object
    # equality. 
    # for each element in list:
    #        if (cmp(val, element) is true:
    # return object

    def lookup(self, val, cmp=None):
        self.iter=self.header.next
        if cmp==None:
            while self.iter!=self.header:
                if self.iter.obj.name==val:
                    return self.iter.obj
                self.iter=self.iter.next    
        else:
            while self.iter!=self.header:
                if cmp(self.iter.obj,val)==True:
                    return self.iter.obj
                self.iter=self.iter.next

    # returns true if list is not empty
    # if it is empty, returns False.

    def not_empty(self):
        if self.size==0:
            return False
        else:
            return True

    def first(self):
        return self.header.next.obj

    # returns last element

    def last(self):
        return self.tail.obj

    # adds the element to 
  
    def add(self, obj):
        """ This functions adds a new element to the list. Here, the value stored in obj can either be a server class object or a vm class object"""
        if self.type != 'list':
                raise Exception("Add op supported only for list")
        else:
            node=myelem(obj)
            node.prev=self.header
            node.next=self.header.next
            self.header.next=node
            if self.size==0:
                self.tail=node
                self.header.prev=self.tail
                self.size+=1
            else:
                self.header.next.prev=node
                self.size+=1
      
    
   
    def push(self, obj):
        """ Used to push elements to stack. The obj can be a vm class object or a server class object"""
        if self.type != 'stack':
            raise Exception("push op supported only for stack")
        else:
            node=myelem(obj)
            node.obj=obj
            if self.size==0:
                node.prev=self.header
                node.next=self.header
                self.tail=node  
                self.header.next=node
                self.header.prev=self.tail
                self.size+=1

            else:
                node.prev=self.header
                node.next=self.header.next
                self.header.next.prev=node
                self.header.next=node
                self.size+=1

            
            
    
    def pop(self):
        """ To pop values from a stack. It will return the server or vm class object"""
        if self.type != 'stack':
            raise Exception("pop op supported only for stack")
        else:
            poppedValue=0
            if self.header!=self.tail:	
                if self.size>1:
                    poppedValue=self.header.next.obj
                    self.header.next.next.prev=self.header
                    self.header.next=self.header.next.next
                else:
                    poppedValue=self.header.next.obj
                    self.header.next=self.header
                    self.header.prev=self.header
                    self.tail=self.header
                self.size-=1
                return poppedValue
    # give the peek value of the stack as per definition

    
    
    def peek(self):
        if self.type != 'stack':
            raise Exception("peek op supported only for stack")
        else:
            return self.header.next.obj

        

    def enqueue(self, obj):
        if self.type != 'queue':
            raise Exception("Enqueue op supported only for queue")
        else:
            node=myelem(obj)
            node.next=self.header
            if self.size==0:
                node.prev=self.header
                self.header.next=node
                self.tail=node
                self.header.prev=self.tail
                self.size+=1
            else:
                node.prev=self.tail
                self.tail.next=node
                self.tail=node
                self.size+=1


    def dequeue(self):
        if self.type != 'queue':
            raise Exception("Dequeue op supported only for queue")
        else:
            if self.header!=self.tail:
                if self.size>1:
                    dequeued=self.header.next.obj
                    self.header.next=self.header.next.next
                    self.header.next.next.prev=self.header
                else:
                    dequeued=self.header.next.obj
                    self.header.next=self.header
                    self.header.prev=self.header
                    self.tail=self.header
                self.size-=1
                return dequeued

   
   # works for all of the three types.

    def delete(self, obj):
        foundFlag=0
        iterObject=self.header.next
        while iterObject!=self.header:
            if iterObject.obj==obj:
                previous=iterObject.prev
                nex=iterObject.next
                previous.next=iterObject.next
                nex.prev=iterObject.prev
                if iterObject==self.tail:
                    self.tail=self.tail.prev
                self.size-=1

                break 
            iterObject=iterObject.next

        
        

    # iterator objects for all.
    
    def __iter__(self):
        self.iter=self.header.next
        return self
    
    def __next__(self):
        if self.iter!=self.header:
            value=self.iter.obj
            self.iter=self.iter.next
            return value
        else:
            raise StopIteration
        
    def __str__(self):
        s=''
        h=self.header
        e=self.header.next
        s=f'List size: {self.size}'
        s += '\n'
        while e != h:
            s += f'{e.obj}'
            if (e.next != h):
                s += '\n'
            e = e.next
        s += '\n'
#       if e.prev != self.tail:
#            s += f'tail corrupt: tail: {self.tail.obj} list tail: {e.prev.obj}'

        if self.tail != self.header:
            s += f'Tail: {self.tail.obj}'
        s += '\n\n'
        return s
             

def main():
    pass

if __name__ == "__main__":
    main()

    
    
    
