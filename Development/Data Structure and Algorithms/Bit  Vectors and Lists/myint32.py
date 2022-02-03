
from mem import myMemory

mem=myMemory(1,'KB')

class myint32():
    def __init__(self, value):
        if (value > mem.uint32max):
            print('Value out of range')
        self.p = mem.store_int32(value)
        self.s = 4
        self.v=value

    def __str__(self):
        return (str(self.v))




