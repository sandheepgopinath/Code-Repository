import mymemory as mymem
import ctypes
from ctypes import *
class mystr:

    # implement the init
    # self.mymemobj = mymem.getmymemobj()
    # self.p = allocate the right space with type as this class name string
    # see myclass mem_alloc function
    # size is implemented as "s" property of the object implement gets
    # so that obj.s gives the size of this object.
    # value obj.v is implemented as getv and setv property functions

    def number_to_letter(self,number):
        return chr(int(number))
        
        
    def __init__(self, value):
        self.mymemobj = mymem.getmymemobj()
        self.len=len(value)
        self.byte_array=['0'+bin(ord(letter))[2:] for letter in value]
        self.ptr=self.mymemobj.mem_alloc(self.len,'mybyte')
        self.location=int(self.ptr,16)-int(self.mymemobj.start)
        self.interalAddress=self.mymemobj.internalPointer+self.location
        self.memory_array=(ctypes.c_ubyte*self.len).from_address(self.interalAddress)       
        
        for i in range(self.len):
            self.memory_array[i]=int(self.byte_array[i],2)

# get the value of the string  same as it was initialized with or later set.

    def getv(self):
        string=''
        for i in range(self.len):
            string+=self.number_to_letter(self.memory_array[i])
        return string 

# set the new value for string

    def setv(self, value):
        self.byte_array=['0'+bin(ord(letter))[2:] for letter in value]
        self.len=len(value)
        self.memory_array=(ctypes.c_ubyte*self.len).from_address(self.interalAddress)       
        
        for i in range(self.len):
            self.memory_array[i]=int(self.byte_array[i],2) 

# return the size occupied by the string
# in bytes

    def gets(self):
        return self.len 

    def __del__(self):
    	self.mymemobj.mem_free(self.ptr,self.len,'mybyte') 

    v = property(getv, setv, None, "I'm the 'value' property.")
    s = property(gets, None, None, "I'm the 'value' property.")

