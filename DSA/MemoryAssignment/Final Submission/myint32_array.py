import mymemory as mymem
import ctypes
from ctypes import *
## myint32_array implementation.

class myint32_array:

    # implement the init
    # self.mymemobj = mymem.getmymemobj()
    # self.p = allocate the right space with type as 'myint32_array'
    # see myclass mem_alloc function
    # self.len = size of the myint32_array (no. of elements)

    def __init__(self, size, init=0):
        self.mymemobj = mymem.getmymemobj()
        self.len=size
        self.size=size*4
        self.p=self.mymemobj.mem_alloc(size,'myint32_array')
        self.location=int(self.p,16)-int(self.mymemobj.start)
        self.interalAddress=self.mymemobj.internalPointer+self.location
        self.array=(ctypes.c_ubyte*size).from_address(self.interalAddress)
        self.n=-1
        for i in range(size):
            ptr=self.mymemobj.store_int32(init,hex(int(self.p,16)+(i*4)))
            
# A[i] will work with this function. returns the ith element.
# Ensure to raise Exception("Array out of index Exception") if the element
# goes out of bound.

    def __getitem__(self, i):
    	if i>self.len:
    		raise Exception('Array out of index Exception')
    	else:
        	i=i*4
        	print(self.mymemobj.load_int32(hex(int(self.p,16)+(i))))

# A[i] =5 will work with this function. returns the ith element.
# Ensure to raise Exception("Array out of index Exception") if the element
# goes out of bound.

    def __setitem__(self, i, value):
    	if i>self.len:
    		raise Exception('Array out of index Exception')
    	else:
        	ptr=self.mymemobj.store_int32(value,hex(int(self.p,16)+(i*4)))
# iterator function store whatever is required in self for iterating in
# combination with __next__ function.
# see example code in assignment unit that I added.

    def __iter__(self):
        return self

# next function for iterator raises StopIteration once all array elements
# are iterated upon.

    def __next__(self):
        if self.n<self.len-1:
            self.n+=1
            return self.mymemobj.load_int32(hex(int(self.p,16)+(4*self.n)))
        else:
            raise StopIteration
# get the property "s" 
# A.s as defined inthe spec by this function.

    def gets(self):
        return self.size

# Free the element when this is called by garbage collector.
# right size etc.

    def __del__(self):
        self.mymemobj.mem_free(self.p,self.len,'myint32_array')

    s = property(gets, None, None, "I'm the 'value' property.")

