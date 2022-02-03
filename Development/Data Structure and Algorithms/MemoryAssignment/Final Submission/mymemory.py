from myerror import *
from ctypes import *
from mybit_vector import *

# exceptions for mymemory class
# need not edit these exceptions, keep it as is

class mymem_error(myerror):
    pass

class mymem_bad(mymem_error):
    def __init__(self, size, message="size not aligned or large"):
        self.size=size
        self.message=message
    def __str__(self):
        return f'{self.size} -> {self.message}'

class mymem_occupied(mymem_error):
    def __init__(self, ptr, message="memory already occupied"):
        self.ptr=ptr
        self.message=message
    def __str__(self):
        return f'{self.ptr} -> {self.message}'
    
class mymem_nomem(mymem_error):
    def __init__(self, mymem,memsize,allocated,free, message="Memory NOT AVAILABLE"):
        self.mymem = mymem
        self.message=message
        self.memsize=memsize
        self.allocated1=allocated
        self.free1=free
    def __str__(self):
        return f'memtotal: {self.memsize} allocated: {self.allocated1} free: {self.free1}  -> {self.message}'

class mymem_invalidptr(mymem_error):
    def __init__(self, ptr, mymem, message="invalid memory ptr"):
        self.ptr=ptr
        self.ptr1=mymem.start
        self.ptr2=mymem.end
        self.message=message
    def __str__(self):
        return f'ptr: {self.ptr} ptr should be between:{self.ptr1} and {self.ptr2} -> {self.message}'

class mymem_badval(mymem_error):
    def __init__(self, val, message="bad or large value"):
        self.val=val
        self.message=message
    def __str__(self):
        return f'{self.val} -> {self.message}'

class mymem_invalid_alloctype(mymem_error):
    def __init__(self, type, mymem, message="invalid alloc type"):
        self.type=type
        self.mymem=mymem
        self.message=message
    def __str__(self):
        return f'type: {self.type} not in {self.mymem.types}-> {self.message}'

class mymem_corrupt(mymem_error):
    def __init__(self, ptr, nbytes=0, b=0, i=0, message="memory corrupted"):
        self.ptr=ptr
        self.nbytes=nbytes
        self.b=b
        self.i=i
        self.message=message
    def __str__(self):
        return f'ptr: {self.ptr} nbytes: {self.nbytes} b: {self.b} i: {self.i} -> {self.message}'

#implementation of mymemory class
# and all its methods

class mymemory():
    maxsize=1024*1024*1024
    int32_max=pow(2,31)-1
    int32_min=pow(2,31)*-1
    int64_max=pow(2,63)-1
    int64_min=pow(2,63)*-1
    byte_min=0
    byte_max=255

    # members:
    # byte_arr = linear memory array
    # start and end pointers for memory addresses handed out to callers.
    # The pointers map to the byte_arr index linearly.
    # current stores the current value of the index in the byte_arr from where
    # you will look for available memory in the byte_arr.
    # memsize = total memory size given by the test.py file or whoever uses it.
    # bv is the bitvector implementation object
    # free = total free memory (initial value is all memory is free)
    # allocated = total allocated memory (initial value is zero
    # alloc_types is a dictionary for storing what memory went to what data type
    # indicated by the mem_alloc and mem_free last argument strings. they
    # should be same as the self.types defined here. 
    # this helps in seeing who allocated how much and if there is a memory
    # leak you can figure it out.
    
    def __init__(self, size):
        if size > self.maxsize:
            raise mymem_bad(size)
        self.byte_arr=(c_ubyte*size)()
        self.start=0xfffffffc00000000
        self.end=self.start+size
        self.current = 0;
        self.memsize=size
        self.bv =  mybit_vector(size)
        self.free=size
        self.allocated=0
        self.alloc_types={}
        self.types=['mybyte','mybool','myint32','myint64','mystr', 'myint32_array', 'myint64_array']
        self.memory_usage={'mybyte':1,'mybool':1,'myint32':1,'myint64':1,'mystr':1,'myint32_array':8,'myint64_array':8}
        self.internalPointer=ctypes.addressof(self.byte_arr)
        for t in self.types:
            self.alloc_types[t]=0

# checks if the pointer is valid

    def ptr_check(self, ptr):
        if (ptr <self.start or ptr >= self.end):
            raise mymem_invalidptr(ptr, self)

# converts memory pointer value to index into byte_arr
# use this function in mem_free and in load_zzz
# and in store_zzz functions

    def ptr_to_index(self, ptr):
        self.ptr_check(ptr)
        return ptr-self.start

# converts index in byte_arr to memory pointer 
# this is just a linear mapping as you see.
# clients only see the memory pointer they dont understand the implementation
# of byte array index etc.
# use this function to convert the index to ptr in mem_alloc

    def index_to_ptr(self, index):
        ptr=self.start+index
        self.ptr_check(ptr)
        return ptr

# allocates memory for nbytes
# type should be one of types indicated above.
# returns memory pointer (not the index to byte arr)
# uses bit vector self.bv to invoke the right methods.
# raises mymem_nomem(self) exception if you dont find the 
# required memory.
# do the book keeping appropriately for allocated, free and alloc_types

        
    def mem_alloc(self, nbytes, type):
        if type not in self.types:
            raise mymem_invalid_alloctype(type, self)
        else:
            free_index=self.bv.find_freespace(nbytes)
            if free_index!=None: # If free space is found
                for i in range(free_index,free_index+nbytes):
                    self.bv.set_bit(i)
                self.alloc_types[type]+=(nbytes*self.memory_usage[type])
                self.current=hex(int(self.start)+free_index)
                self.free-=int(nbytes*self.memory_usage[type])
                self.allocated+=int(nbytes*self.memory_usage[type])
                return self.current
        
            else:
                memError=mymem_nomem(nbytes,self.memsize,self.allocated, self.free)
                print(memError)
                

# free the memory at ptr for nbytes, for the type strings mentioned above.
# do the book keeping appropriately for allocated, free and alloc_types
# raises mymem_invalid_alloctype if type is not part of the string above.

    def mem_free(self, ptr, nbytes, type):
        if type not in self.types:
            raise mymem_invalid_alloctype(type, self)
        else:
            self.free+=nbytes
            self.allocated-=nbytes
            
            #print(self.memsize,self.free,self.allocated)
            delete_index=int(ptr,16)-int(self.start)
            for i in range(delete_index,delete_index+nbytes):
                self.bv.clear_bit(i)
            
            
            
    def addressTranslation(self,ptr):
        """ Converts the start address into the memory address returned by the ctypes"""
        position=int(ptr,16)-int(self.start)
        return hex(int(self.internalPointer)+position)
        
        
       
# returns the value of the byte at ptr.

    def load_byte(self, ptr):
        self.ptr_check(int(ptr,16))
        ptr=self.addressTranslation(ptr)
        array=(ctypes.c_ubyte*1).from_address(int(ptr,16))
        if (int(array[0]) >self.byte_max) | (int(array[0]) <self.byte_min):
            bad_value=mymem_badval()
            print(bad_value)
        else:
            return int(array[0])

# stores the byte at ptr and if ptr is None, allocates memory for a byte
# and stores the value and returns. If ptr is not None it stores the value
# at pointer.

    def store_byte(self, value, ptr=None):
        
        stopExecution=0
        if ptr != None:
            self.ptr_check(int(ptr,16))   
            if (int(ptr,16)+1>int(self.start)) & (int(ptr,16)+1<int(self.end)):
                positionInMemory=int(ptr,16)-int(self.start) # Calculating the memory address using the given pointer
                location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.start+location
                if self.bv.is_free(location)==0:
                    stopExecution=1
                    occupied_object=mymem_occupied(ptr)
                    print(occupied_object)
                else:
                    pass
            else:
                stopExecution=1
                invalid_ptr=mymem_invalidptr(ptr,self)
                print(invalid_ptr)
        else:
            ptr=self.mem_alloc(1,'mybyte')
            positionInMemory=int(ptr,16)-int(self.start) # Calculating the memory address using the given pointer
            location=int(positionInMemory/8)+int(positionInMemory%8)
            
            
        if stopExecution==0:
            if value<=255:
                self.byte_arr[location]=value
                self.free-=1
                self.allocated+=1
                return ptr
            else:
                print('Invalid value for Byte ( Enter value between 0 and 255)')
                bad_value=mymem_badval(value)
                print(bad_value)
      





# returns the value of the int32 at ptr.
# raises mymem_badval(value) exception if the value overflows on both sides
# negative or positive. (note this is only possible due to your bug as
# store_int32 checks the value for exactly the same.

    def load_int32(self,ptr):
        self.ptr_check(int(ptr,16))
        location=int(ptr,16)-int(self.start)
        
        binary=''
        for i in range(location,location+4):
            temp=str(bin(self.byte_arr[i]))[2:]
            if len(temp)<8:
                temp='0'*(8-len(temp))+temp
            binary+=str(temp)

        if binary[0]=='1':
            return int(binary[1:],2)*-1
        else:
            return int(binary[1:],2)
    


        
        
# stores the int32 at ptr and if ptr is None, allocates memory for the size
# of int32 bytes stores the value and returns. If ptr is not None it stores the value
# at pointer.
# raises mymem_badval(value) exception if the value overflows on both sides
# negative or positive.
# stores value in little indian format. (x86 way)


    def store_int32(self, value, ptr=None):
        stopExecution=0
        if ptr != None:
            self.ptr_check(int(ptr,16))
               
            if (int(ptr,16)+4>int(self.start)) & (int(ptr,16)+4<int(self.end)):
                positionInMemory=int(ptr,16)-int(self.start) # Calculating the memory address using the given pointer
                location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.start+positionInMemory
   
            else:
                stopExecution=1
                invalid_ptr=mymem_invalidptr(ptr,self)
                raise invalid_ptr
        else:
            ptr=self.mem_alloc(4,'myint32')
            positionInMemory=int(ptr,16)-int(self.start) # Calculating the memory address using the given pointer
            location=int(positionInMemory/8)+int(positionInMemory%8)
            ptr=self.start+positionInMemory

        if stopExecution==0:
            limits=(self.int32_min,self.int32_max)
            # Checks if the number is within the range of Signed Int
            if limits[0]<=value<=limits[1]:
                binary=''
                if len(bin(value)[2:])<=32:
                    if value<0:
                        binary='0'*(31-len(bin(value)[3:]))+bin(value)[3:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='1'+binary
                    elif value>=0:
                        binary='0'*(31-len(bin(value)[2:]))+bin(value)[2:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='0'+binary
                # Storing the binary into memory, byte by byte
                pos=positionInMemory
                for i in range(0,32,8):
                    self.byte_arr[pos]=int(binary[i:i+8],2)
                    pos+=1   
		
                for i in range(location,location+4):
                    self.bv.set_bit(i)
               
                return hex(self.start+positionInMemory)
            else:
            
            	raise mymem_badval(value)
                

# 
# returns the value of the int64 at ptr.
# raises mymem_badval(value) exception if the value overflows on both sides
# negative or positive. (note this is only possible due to your bug as
# store_int64 checks the value for exactly the same.

    def load_int64(self,ptr):
        self.ptr_check(int(ptr,16))
        location=int(ptr,16)-int(self.start)
        
        binary=''
        for i in range(location,location+8):
            temp=str(bin(self.byte_arr[i]))[2:]
            if len(temp)<8:
                temp='0'*(8-len(temp))+temp
            binary+=str(temp)

        if binary[0]=='1':
            return int(binary[1:],2)*-1
        else:
            return int(binary[1:],2)

# stores the int64 value at ptr and if ptr is None, allocates memory for the size
# of int64 bytes stores the value and returns. If ptr is not None it stores the value
# at pointer.
# raises mymem_badval(value) exception if the value overflows on both sides
# negative or positive.
# stores value in little indian format. (x86 way)

    def store_int64(self, value, ptr=None):
        stopExecution=0
        if ptr != None:
            self.ptr_check(int(ptr,16))
               
            if (int(ptr,16)+8>int(self.start)) & (int(ptr,16)+8<int(self.end)):
                positionInMemory=int(ptr,16)-int(self.start) # Calculating the memory address using the given pointer
                location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.start+positionInMemory
   
            else:
                stopExecution=1
                invalid_ptr=mymem_invalidptr(ptr,self)
                raise invalid_ptr
        else:
            ptr=self.mem_alloc(8,'myint64')
            positionInMemory=int(ptr,16)-int(self.start) # Calculating the memory address using the given pointer
            location=int(positionInMemory/8)+int(positionInMemory%8)
            ptr=self.start+positionInMemory

        if stopExecution==0:
            limits=(self.int64_min,self.int64_max)
            # Checks if the number is within the range of Signed Int
            if limits[0]<=value<=limits[1]:
                binary=''
                if len(bin(value)[2:])<=64:
                    if value<0:
                        binary='0'*(63-len(bin(value)[3:]))+bin(value)[3:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='1'+binary
                    elif value>=0:
                        binary='0'*(63-len(bin(value)[2:]))+bin(value)[2:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='0'+binary
                # Storing the binary into memory, byte by byte
                pos=positionInMemory
                for i in range(0,64,8):
                    self.byte_arr[pos]=int(binary[i:i+8],2)
                    pos+=1   

                for i in range(location,location+4):
                    self.bv.set_bit(i)
                return hex(self.start+positionInMemory)
            else:
                raise mymem_badval(value)
                
# leave it as is it prints all values for testing purposes etc.

    def __str__(self):
        s=f'memtotal: {self.memsize} allocated: {self.allocated} free: {self.free}'
        s+= '\n'
        s+=f'membyalloctypes: {self.alloc_types}'
        s+= '\n'
        s1=f'start: {hex(self.start)} end: {hex(self.end)} current: {self.current}'
        s=s+s1
        return s

# the following helps get the memobj by the clients ie. the individual
# classes.

mymemobj=mymemory(1024)


def getmemobj(size):
    global mymemobj
    if mymemobj:
        return mymemobj
    mymemobj=mymemory(size)
    return mymemobj
     

def getmymemobj():
	return mymemobj
          
