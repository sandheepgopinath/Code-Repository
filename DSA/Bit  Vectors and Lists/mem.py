

class bit_vector(int size):
    def __init__(self, size):
        # initialize size "bits" in some python specific data structure.
        # it could be alist of bools may be
        # syntax you figure out astate= (False * size)[]
        # if it is False it is free
        # if it is True it is allocated.
        # this is a bit map.
        # instead of boolean I will use integers and use bit operators
        # to figure this.
        # because python supports large integers it could also be for eg.
        # int bits= 1<< (size+1) 
        # that means you could use simple bit logic  to figure if the bit is
        # set or not.
        # infat bit vector is a data structure 
        # using bits will be efficient for space. dont use integer. 
        # do not use any available classes.
        # you could also ctype. 
        #infact i suggest using c_ubyte the way we allocate linear bytes
        # allocate the byte for the bit vector ie. 128MB max. Do not hard code 
        # anything.
       return

    def is_free(int byteaddr):
        # figure out if the corresponding bit is True or False.

    def set_bit(int byteaddr):

class mymemory():

    int32_max = (pow(2,31)-1)
    int32_min = -int32_max

    def __init__(self, int memsize):
        mem_arr = as defined in the content of getting a linear array of bytes.
        self.start=0xfffffffc00000000
        self.end = self.start+size
        self.size = size
        self.free = size
        self.mem_alloc_state = bit_vector(memsize/8)
        self.mem_int32_alloc
        self.mem_int64_alloc
        self.mem_alloc


        # initialize the allocation state.
        # helper bitvector.siz
        pass

    def convert_ptr_to_int32(int ptr):
        b1=self.mem_arr[ptr]
        b2=self.mem_arr[ptr]
        b3=self.mem_arr[ptr]
        b4=self.mem_arr[ptr]

        if 8th bit of b4 is 1 
            negative = 1
                  
        int32value = function(b1, b2, b3, b4)

        if (negative)
            int32value = -int32value

        return Int32value;

    def convert_int32_to_bytes(int32value):

        return (b1, b2,b3, b4)

    def is_valid_ptr(int ptr):
        ptr > self.start, and ptr < self.start + self.memsize ->ptr is valid.
        else ptr is invalid.
        return the true or false based on that logic.

    def mem_alloc(int nbytes):
        # for memorysize if nbytes are free contiguously
        # return the starting address of that memory.
        # if bits 8, 9, 10 11 are free ie., 0 
        # ptr = start + 8
        # and then you set the bits 8, 9, 10, 11 to 1 saying it is allocated.
        # 
        for range of all bits:
            # find the contiguous range. 
            # break from this loop if you dont find the memory
            # or if you found contiguous nbytes.

        self.free -= nbytes

        return (ptr)

    def load_int32(int ptr):
    
        if  is_valid_ptr(ptr) == False:
            raise exception

        return convert_ptr_to_int32(ptr);
        pass

    def store_int32(int value, int ptr):
        if (ptr === None)
            ptr = self.mem_alloc(4)
            self.mem_int32_alloc += 4

        if (value > int32_max):
            raise "exception value > int32_max")

        b[]=convert_int32_to_bytes(value)
        #store the bytes in a little indian way to the memory array.
        self.mem_arr[ptr-start] =b1
        self.mem_arr[ptr+1-start]=b2
        self.mem_arr[ptr+2-start]=b3
        self.mem_arr[ptr+3-start]=b4

        if value < 0:
            set the 8th bit of b4 to indicate it is negative.






# repeat  the above for 

    def load_int64()
    def store_int64()
    def convert_ptr_to_int64()
    def convert_int64_to_bytes()


