import mem as mymem

class myint32_array()
    def __init__(self, size):
        self.p=mymem.mem_alloc(size*4)
        self.s = size

# this is the magic method for A[i]
    def __set_item__(int index, int value):

        ptr = self.p + index * 4
        return store_int32(value, ptr);

    def 
        return (mymem.load_int64(self.p))

    gets()

