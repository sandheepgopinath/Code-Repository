import mymemory as mymem

class myint32:

    # implement the init
    # self.mymemobj = mymem.getmymemobj()
    # self.p = allocate the right space with type as this class name string
    # see myclass mem_alloc function
    # size is implemented as "s" property of the object implement gets
    # so that obj.s gives the size of this object.
    # value obj.v is implemented as getv and setv property functions

    def __init__(self, value):
        self.mymemobj = mymem.getmymemobj()
        self.value=value
        self.size=4
        self.p=self.mymemobj.store_int32(value)
        
# For Getting the value
    def getv(self):
        return self.value

# for setting the value 

    def setv(self, value):
        self.value=value
        self.p=self.mymemobj.store_int32(value,self.p)
        
# this returns the size of the object

    def gets(self):
        return self.size

# free the memory

    def __del__(self):
        self.mymemobj.mem_free(self.p,4,'myint32')
        
    v = property(getv, setv, None, "I'm the 'value' property.")
    s = property(gets, None, None, "I'm the 'value' property.")

        
# for the value property

   

