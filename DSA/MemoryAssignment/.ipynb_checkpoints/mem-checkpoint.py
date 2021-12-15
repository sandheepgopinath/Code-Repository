#!usr/bin/python3
import ctypes
from ctypes import *
#class myMemory():
#Allocate 1GB of Space for memory


class bit_vector():
    """ Objects
    
        > self.totalMemory : Will contain information about the size of memory for which the vector is created
        > self.arrayLength : Contani information about the length of the bitvector created
        > self.ByteVector  : The memory location stored as an array for easy traversing and assignments
        > self.ArrayPointer: Contains the starting address of the memory allocated
    """
    
    
    
    def __init__(self,memoryInBytes):
        """
        The function initialises a bit vector which allocates space in memory for memoryinBytes/8 bytes
        This vector is used to identify if a memory location is free or occupied
        > The init function will calculate and allocate the space in memory
        > It will store the starting address of this memory location in self.ArrayPointer. 
        > The memory can be accessed anytime by using the self.ArrayPointer
        > The function will also initialise all values in this allocated memory to 0 to remove any junk values
        
        """
        self.totalMemory=memoryInBytes
        self.arrayLength=int(self.totalMemory/8) 
        self.ByteVector=(ctypes.c_ubyte*self.arrayLength)() # Creating the memory 
        for i in range(self.arrayLength):
            if self.ByteVector[i]>0:
                self.ByteVector[i]=0
        self.ArrayPointer=ctypes.addressof(self.ByteVector)
        
        
        
    
    def checkFreeSpace(self,spaceNeeded):
        """ 
        This function scans through the bit vector to see if the required space neeed is 
        available in the memory. It available it returns the position of byte where
        it is available. The address is then calculated from this position
        """
        array=self.ByteVector
        counter=0
        location=0
        flag=0
        for i in range(self.arrayLength):
            if self.ByteVector[i]==0:
                counter+=1
            else:
                counter=0
            if counter==spaceNeeded:
                flag=1
                break
        if flag==1:
            location=i-(spaceNeeded-1)
            self.freeSpace=location
            print('Available at ',self.freeSpace)
            return self.freeSpace
        elif flag==0:
            print('Not available')
            
            
            
            
            
            
    def spaceCalculator(self,typeOfData):
        if typeOfData=='int32':
            self.size=32
            self.bytesNeeded=4
        elif typeOfData=='int64':
            self.size=64
            self.bytesNeeded=8
        elif typeOfData=='bool':
            self.size=1
            self.bytesNeeded=1
    
    
    
class myMemory():
    """Objects :
                self.ptr  : The memory location at which the last store happened 
                self.type : Type of object last stored
    """
        
    def __init__(self,sizeNeeded,unit):
        """ This function is used to calculate memory to be allocated.
        It takes as input two parameters
        unit : Unit of memory ( "KB" - Kilobytes , MB - "MegaBytes" , "GB" - 'Gigabtes'
        size : Size in units to be allocated
              If unit = "MB" and size= "1" , 1024*1024 bytes will be allocated. 
              ie, 1MB will be allocated    
       The function also creates an object of lass bit_vector which initialises a bitvector which 
       gives information about the status of memory. If it is free or occupied.
       
        """
        # Memory calculation done here. 
        self.start=0xfffffffc00000000
        memInBytes=0
        if unit=='KB':
            self.size=sizeNeeded*1024
        elif unit=='MB':
            self.size=sizeNeeded*1024*1024
        elif unit=='GB':
            self.size=sizeNeeded*1024*1024*1024
        else:
            print('Invalid Value of unit')
            print('Use "KB", "MB" or "GB"')
        self.end=self.start+self.size #Calculates the value for endPointer
        self.free=self.size #The free space available
        self.bitVector=bit_vector(self.size) # Creating a bit vector object. 
        self.memory=(ctypes.c_ubyte*self.size)() # Allocating the space 'size' in memory
        self.internalPointer=ctypes.addressof(self.memory)
        self.uint32min=-2147483648
        self.uint32max=2147483647
        self.bytemin=0
        self.bytemax=255
        self.uint64min=-9223372036854775808
        self.uint64max=9223372036854775807
 	
 	
                
                
    def mem_alloc(self,nbytes):
        """ 
        This function takes as input the number of bytes to be allocated and allocates the space in memory
        It also returns the address of the starting location of the memory"""
        #This will call the checkfreespace function in bit_vector class
        #which will scan through the bit vector and return the 
        # location at which free space is available
        self.location=self.bitVector.checkFreeSpace(nbytes)
        if self.location!=None: # If no free space is found, None is returned
            ptr=self.internalPointer+self.location
            self.type='int32'
            self.free-=nbytes
            return ptr
        else:
            print('Memory error. Allocate more memory')
            
        
          
        
    def store_int32(self,value,ptr=None):
        """ This function is used to save an int32 number to a memory location 
        It takes as input two parameters. A number, which is to be saved, 
        the address to which it has to be saved.
        If a pointer is specified, it checks if that location is already occupied or not and then stores that value if not. 
        Else, it checks for free space and allocates the number there and returns the pointer where it is stored. 
        It also updates the self.free so that the reamainng space can be easily identified. 
        """
        
        stopExecution=0
        tempPtr=ptr # Saving a copy of the address passed
        if ptr==None: # If no pointer is passed, find a new free location using the bitVector
            ptr=self.mem_alloc(4)
        else:
            if (int(ptr)+4>int(mem.start)) & (int(ptr)+4<int(mem.end)):
                positionInMemory=int(ptr)-int(self.start) # Calculating the memory address using the given pointer
                self.location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.internalPointer+self.location
                if self.bitVector.ByteVector[self.location]==1:
                    print('Unable to write to location.Already occupied')
                    stopExecution=1
                else:
                    self.free-=4
            else:
                stopExecution=1
                print('Pointer out of Memory')
                
        if stopExecution==0:
            limits=(self.uint32min,self.uint32max)
            # Checks if the number is within the range of Signed Int
            if limits[0]<value<limits[1]:
                
                array=(ctypes.c_ubyte*4).from_address(ptr)
                binary=''
                if len(bin(value)[2:])<=31:
                    if value<0:
                        binary='0'*(31-len(bin(value)[3:]))+bin(value)[3:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='1'+binary
                    elif value>=0:
                        binary='0'*(31-len(bin(value)[2:]))+bin(value)[2:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='0'+binary
                # Storing the binary into memory, byte by byte
                idx=0
                for i in range(0,32,8):
                    array[idx]=int(binary[i:i+8],2)
                    idx+=1   
            
                self.bitVector.ByteVector[self.location]=1
                self.bitVector.ByteVector[self.location+1]=1
                self.bitVector.ByteVector[self.location+2]=1
                self.bitVector.ByteVector[self.location+3]=1
            else:
                print('Out of Range of Signed Integer')  
            return self.start+self.location   
        else:
            return 0,0
           
            
            
    def load_int32(self,int32ptr):
        """ 
        Function to read data from memory, convert it to decimal and to print it.
        It reads the value from memory and converts it into binary. 
        
        After that it checks if the first 
        """
        array=(ctypes.c_ubyte*4).from_address(int32ptr)
        binary=''
        for i in range(4):
            temp=str(bin(array[i]))[2:]
            if len(temp)<8:
                temp='0'*(8-len(temp))+temp
            binary+=str(temp)

        if binary[0]=='1':
            return int(binary[1:],2)*-1
        else:
            return int(binary[1:],2)
    
    
    
    
    def store_int64(self,value,ptr=None):
        """ This function is used to save an int64 number to a memory location 
        It takes as input two parameters. A number, which is to be saved, 
        the address to which it has to be saved.
        If a pointer is specified, it checks if that location is already occupied or not and then stores that value if not. 
        Else, it checks for free space and allocates the number there and returns the pointer where it is stored. 
        It also updates the self.free so that the reamainng space can be easily identified. 
        """
        
        stopExecution=0
        tempPtr=ptr # Saving a copy of the address passed
        if ptr==None: # If no pointer is passed, find a new free location using the bitVector
            ptr=self.mem_alloc(8)
        else:
            if (int(ptr)+8>int(mem.start)) & (int(ptr)+8<int(mem.end)):
                positionInMemory=int(ptr)-int(self.start) # Calculating the memory address using the given pointer
                self.location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.internalPointer+self.location
                if self.bitVector.ByteVector[self.location]==1:
                    print('Unable to write to location.Already occupied')
                    stopExecution=1
                else:
                    self.free-=8
            else:
                stopExecution=1
                print('Pointer out of Memory')
	
        if stopExecution==0:
            limits=(uint64min,self.uint64max)
            # Checks if the number is within the range of Signed Int 64
            if limits[0]<value<limits[1]:
                
                array=(ctypes.c_ubyte*8).from_address(ptr)
                binary=''
                if len(bin(value)[2:])<=63:
                    if value<0:
                        print('negative')
                        binary='0'*(63-len(bin(value)[3:]))+bin(value)[3:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='1'+binary
                    elif value>=0:
                        binary='0'*(63-len(bin(value)[2:]))+bin(value)[2:]# Since it is unsigned, we can accomodate 32 bits as sign bit is absent
                        binary='0'+binary
                # Storing the binary into memory, byte by byte
                idx=0
                for i in range(0,64,8):
                    array[idx]=int(binary[i:i+8],2)
                    idx+=1   
                self.bitVector.ByteVector[self.location]=1
                self.bitVector.ByteVector[self.location+1]=1
                self.bitVector.ByteVector[self.location+2]=1
                self.bitVector.ByteVector[self.location+3]=1
                self.bitVector.ByteVector[self.location+4]=1
                self.bitVector.ByteVector[self.location+5]=1
                self.bitVector.ByteVector[self.location+6]=1
                self.bitVector.ByteVector[self.location+7]=1
            else:
                print('Out of Range of Signed Integer')  
            return self.start+self.location   
        else:
            return 0,0
           
    
    
    
    def load_int64(self,int64ptr):
        """ 
        Function to read data from memory, convert it to decimal and to print it.
        It reads the value from memory and converts it into binary. 
        
        After that it checks if the first 
        """
        array=(ctypes.c_ubyte*8).from_address(int64ptr)
        binary=''
        for i in range(8):
            temp=str(bin(array[i]))[2:]
            if len(temp)<8:
                temp='0'*(8-len(temp))+temp
            binary+=str(temp)
        if binary[0]=='1':
            return int(binary[1:],2)*-1
        else:
            return int(binary[1:],2)
    
    
    def store_bool(self,value,ptr=None):
        """ This function is used to save an boolean to a memory location 
        It takes as input two parameters. A number, which is to be saved, 
        the address to which it has to be saved.
        If a pointer is specified, it checks if that location is already occupied or not and then stores that value if not. 
        Else, it checks for free space and allocates the number there and returns the pointer where it is stored. 
        It also updates the self.free so that the reamainng space can be easily identified. 
        """
           
        stopExecution=0
        tempPtr=ptr # Saving a copy of the address passed
        if ptr==None: # If no pointer is passed, find a new free location using the bitVector
            ptr=self.mem_alloc(1)
        else:
            if (int(ptr)+1>int(mem.start)) & (int(ptr)+1<int(mem.end)):
                positionInMemory=int(ptr)-int(self.start) # Calculating the memory address using the given pointer
                self.location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.internalPointer+self.location
                if self.bitVector.ByteVector[self.location]==1:
                    print('Unable to write to location.Already occupied')
                    stopExecution=1
                else:
                    self.free-=1
            else:
                stopExecution=1
                print('Pointer out of Memory')

        if stopExecution==0:
            array=(ctypes.c_ubyte*1).from_address(ptr)
            if value==1:
                array[0]=1
            elif value==0:
                array[0]=0
            else:
                print('Invalid value for Boolean')
                
            self.bitVector.ByteVector[self.location]=1 
            return self.start+self.location  
        else:
            return 0,0
           
    
    
        
    def load_bool(self,boolPtr):
        """ 
        Function to read data from memory, convert it to decimal and to print it.
        It reads the value from memory and converts it into binary. 
        
        After that it checks if the first 
        """
        array=(ctypes.c_ubyte*1).from_address(boolPtr)
        binary=''
        return int(array[0])
    
    def is_valid_(self,ptr):
        if (int(ptr)>int(mem.start)) & (int(ptr)<int(mem.end)):
            return True
        else:
            return False
    
    def mem_status(self):
        print('Total memory allocated : ',self.size)
        print('Total free memory      : ',self.free)
        print('Total used memory      : ',self.size-self.free)
        
        print('Size of int32          : 4 bytes')
        print('Size of int64          : 8 bytes')
        print('Size of bool           : 1 bytes')
        print('Size of byte           : 1 bytes')
        
        return(self.size,self.free,self.size-self.free,4,8,1,1)
        
    
    def store_byte(self,value,ptr=None):
            
        stopExecution=0
        tempPtr=ptr # Saving a copy of the address passed
        if ptr==None: # If no pointer is passed, find a new free location using the bitVector
            ptr=self.mem_alloc(1)
        else:
            if (int(ptr)+1>int(mem.start)) & (int(ptr)+1<int(mem.end)):
                positionInMemory=int(ptr)-int(self.start) # Calculating the memory address using the given pointer
                self.location=int(positionInMemory/8)+int(positionInMemory%8)
                ptr=self.internalPointer+self.location
                if self.bitVector.ByteVector[self.location]==1:
                    print('Unable to write to location.Already occupied')
                    stopExecution=1
                else:
                    self.free-=1
            else:
                stopExecution=1
                print('Pointer out of Memory')

        if stopExecution==0:
            array=(ctypes.c_ubyte*1).from_address(ptr)
            if value<=255:
                array[0]=value
            else:
                print('Invalid value for Byte ( Enter value between 0 and 255')
                
            self.bitVector.ByteVector[self.location]=1 
            return self.start+self.location   
        else:
            return 0,0
           
    
    
        
    def load_byte(self,boolPtr):
        """ 
        Function to read data from memory, convert it to decimal and to print it.
        It reads the value from memory and converts it into binary. 
        
        After that it checks if the first 
        """
        array=(ctypes.c_ubyte*1).from_address(boolPtr)
        binary=''
        return int(array[0])
    
