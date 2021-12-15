from mybit_vector import *
from mymemory import *
from myint32 import *
from myint64 import *
from mystr import *
from myint32_array import *
from myint64_array import *
from os import sys


def bit_vector_tests():
    bv=mybit_vector(48)

# verify that all bits are zero

    print(bv)

    bv.set_bit(3)
    print(bv)

    bv.set_bit(47)
    print(bv)

    try:
        bv.set_bit(48)
        print(bv)

    except mybit_overflow:
        print("overflow test passed")

    if bv.is_set(47):
        print("47 set bit passed")
    else:
        print("47 set bit FAILED")
        sys.exit(1)

    if bv.is_free(47) == 0:
        print("47 ! clear bit passed")
    else:
        print("47 ! clear bit FAILED")
        sys.exit(1)

    if bv.is_set(3):
        print("3 set bit passed")
    else:
        print("3 set bit FAILED")
        sys.exit(1)
    if bv.is_free(3) == 0:
        print("3 ! clear bit passed")
    else:
        print("3 ! clear bit FAILED")
        sys.exit(1)

    print(bv)
    bv.clear_bit(47)
    bv.clear_bit(3)
    print(bv)
    print("PLEASE VERIFY THAT all bits are zero in the above VECTOR ")

def myint32_tests():
    global mymemobj
    a=myint32(5)
    print(a.v)
    if a.v !=5:
        print("myint32 init-get FAILED")
        sys.exit(1)
    else:
        print("myint32 init-get PASSED")

    if a.s != 4:
        print(f'myint32 size test FAILED')
        sys.exit(1)
    else:
        print(f'myint32 size test PASSED')

    a.v=6
    if a.v !=6:
        print("myint32 set FAILED")
        sys.exit(1)
    else:
        print("myint32 set PASSED")

    a.v=-10
    if a.v != -10:
        print("myint32 set-get FAILED for -10")
        sys.exit(1)
    else:
        print("myint32 set-get PASSED for -10")

    a.v=10
    if a.v != 10:
        print("myint32 set-get FAILED for 10")
        sys.exit(1)
    else:
        print("myint32 set-get PASSED for 10")


    for i in range(0,pow(2,31)-1,10000):
        a.v=i
        if a.v != i:
            print(f'myint32 set-get FAILED for {i}')
            sys.exit(1)
        if i and i%1000000000 == 0:
            print(f'myint32_test: done until i: {i}')

    print(f'myint32_test positive looptest PASSED')
    
    for i in range(0,pow(2,31)-1,10000):
        a.v=-i
        if a.v != -i:
            print(f'myint32 set-get FAILED for {i}')
            sys.exit(1)
        if i and i%1000000000  == 0:
            print(f'myint32_test: done until i: {-i}')
    print(f'myint32_test negative looptest PASSED')

    ae=0
    try:
        a.v=pow(2,31)+2
    except mymem_badval:
        print(f'myint32 positive overflow test passed for {pow(2,31)+2}')
        ae=1
    if ae != 1:
        print (f'myint32 got BAD exception for positive overflow should return mymem_badval: FAILED')
        sys.exit(1)
    ae=0
    try:
        a.v=-(pow(2,31)+2)
    except mymem_badval:
        print(f'myint32 negative overflow test passed for {pow(2,31)+2}')
        ae=1
    if ae != 1:
        print (f'myint32 got BAD exception for negative overflow should return mymem_badval: FAILED ')
        sys.exit(1)

    # memory allocated and the allocated for this type should be equal
    # to whatever objects we defined above. when this function returns
    # they will go out of scope and get freed eventually. 
    # verify that allocated in this print shows up the right values.
    print(mymemobj)

def myint64_tests():
    global mymemobj
    a=myint64(5)
    if a.v !=5:
        print("myint64 init-get FAILED")
        sys.exit(1)

    if a.s != 8:
        print(f'myint64 size test FAILED')
        sys.exit(1)
    else:
        print(f'myint64 size test PASSED')
    a.v=6
    if a.v !=6:
        print("myint64 set FAILED")
        sys.exit(1)

    a.v=-10
    if a.v != -10:
        print("myint64 set-get FAILED for -10")
        sys.exit(1)
    a.v=10
    if a.v != 10:
        print("myint64 set-get FAILED for 10")
        sys.exit(1)


#change this if to 0 condition if you want to disable it for 
# debugging.
    if 1:
        for i in range(0,pow(2,63)-1,100000000000000):
            a.v=i
            if a.v != i:
                print(f'myint64 set-get FAILED for i')
                sys.exit(1)
            if i and i%1000000000000000000 == 0:
                print(f'myint64: done until i: {i}')
        print(f'myint64_test positive looptest PASSED')
        for i in range(0,pow(2,63)-1,100000000000000):
            a.v=-i
            if a.v != -i:
                print(f'myint64 set-get FAILED for {-i}')
                sys.exit(1)
            if i and i%1000000000000000000 == 0:
                print(f'myint64: done until i: {-i}')
        print(f'myint64_test negative looptest PASSED')

    ae=0
    try:
        a.v=pow(2,63)+2
    except mymem_badval:
        print(f'myint64 positive overflow test passed for {pow(2,63)+2}')
        ae=1
    if ae != 1:
        print (f'myint64 got BAD exception for positive overflow should return mymem_badval FAILED')
        sys.exit(1)
    ae=0
    try:
        a.v=-(pow(2,63)+2)
    except mymem_badval:
        print(f'myint64 negative overflow test passed for {-pow(2,63)+2}')
        ae=1
    if ae != 1:
        print (f'myint64 got BAD exception for negative overflow should return mymem_badval FAILED ')
        sys.exit(1)

    # memory allocated and the allocated for this type should be equal
    # to whatever objects we defined above. when this function returns
    # they will go out of scope and get freed eventually. 
    # verify that allocated in this print shows up the right values.
    print(mymemobj)

def mystr_tests():
    global mymemobj

    ms=mystr("srini")
    print(ms.v)
    if ms.v != "srini":
        print(f'mystr value test FAILED ')
        sys.exit(1)
    else:
        print(f'mystr value test PASSED ')

    print(ms.s)
    if ms.s != 5:
        print(f'mystr size test FAILED ')
        sys.exit(1)
    else:
        print(f'mystr size test PASSED ')

    ms.v="destroy"
    print(ms.v)
    print(ms.s)
    if ms.v != "destroy":
        print(f'mystr value set test FAILED ')
        sys.exit(1)
    else:
        print(f'mystr value set test PASSED ')
    if ms.s != 7:
        print(f'mystr changed size test FAILED ')
        sys.exit(1)
    else:
        print(f'mystr changed size test PASSED ')

    # memory allocated and the allocated for this type should be equal
    # to whatever objects we defined above. when this function returns
    # they will go out of scope and get freed eventually. 
    # verify that allocated in this print shows up the right values.
    print(mymemobj)


def myint32_aray_tests():
    global mymemobj

    A=myint32_array(5, pow(2,31)-1)

    print(A[2])
    for i in A:
        print(i)
        if i != pow(2,31)-1:
            print(f'myint32_array: initialization value test FAILED')
            sys.exit(1)
    print(f'myint32_array: initialization value test PASSED')
    print(f'Len: {A.s}')
    if A.s != 20:
        print(f'myint32_array: size test FAILED')
        sys.exit(1)
    else:
        print(f'myint32_array: size test PASSED')
        
    ae=0
    try:
        A[1000]
    except Exception as e:
        print(e)
        print("myint32_array out of index Exception test PASSED")
        ae=1
    if ae != 1:
        print("myint32_array out of index Exception test FAILED")
        sys.exit(1)
    ae=0
    try:
        A[2]=pow(2,31)+2
    except mymem_badval:
        print(f'myint32_array element  positive overflow test PASSED for {pow(2,31)+2}')
        ae=1
    if ae != 1:
        print(f'myint32_array element  positive overflow test FAILED for {pow(2,31)+2}')
        sys.exit(1)
    ae=0
    try:
        A[2]=-(pow(2,31)+2)
    except mymem_badval:
        print(f'myint32_array element  negative overflow test passed for {pow(2,31)+2}')
        ae=1
    if ae != 1:
        print(f'myint32_array element  negative overflow test FAILED for {pow(2,31)+2}')
        sys.exit(1)

    # memory allocated and the allocated for this type should be equal
    # to whatever objects we defined above. when this function returns
    # they will go out of scope and get freed eventually. 
    # verify that allocated in this print shows up the right values.

    print(mymemobj)

def myint64_aray_tests():
    global mymemobj

    A=myint64_array(5, pow(2,63)-1)

    print(A[2])
    for i in A:
        print(i)
        if i != pow(2,63)-1:
            print(f'myint64_array: initialization value test FAILED')
            sys.exit(1)
    print(f'myint64_array: initialization value test PASSED')
    print(f'Len: {A.s}')
    if A.s != 40:
        print(f'myint64_array: size test FAILED')
        sys.exit(1)
    else:
        print(f'myint64_array: size test PASSED')

    ae=0
    try:
        A[1000]
    except Exception as e:
        print(e)
        print("myint64_array: out of index Exception test PASSED")
        ae=1
    if ae != 1:
        print("myint64_array out of index Exception test FAILED")
        sys.exit(1)
    ae=0
    try:
        A[2]=pow(2,63)+2
    except mymem_badval:
        print(f'myint64_array element  positive overflow test PASSED for {pow(2,63)+2}')
        ae=1
    if ae != 1:
        print(f'myint64_array element  positive overflow test FAILED for {pow(2,63)+2}')
        sys.exit(1)
    ae=0
    try:
        A[2]=-(pow(2,63)+2)
    except mymem_badval:
        print(f'myint64_array element  negative overflow test PASSED for {pow(2,63)+2}')
        ae=1
    if ae != 1:
        print(f'myint64_array element  negative overflow test FAILED for {pow(2,63)+2}')
        sys.exit(1)

    # memory allocated and the allocated for this type should be equal
    # to whatever objects we defined above. when this function returns
    # they will go out of scope and get freed eventually. 
    # verify that allocated in this print shows up the right values.

    print(mymemobj)

global mymemobj

def main():
    global mymemobj
    #bit vector tests
    #print running bit vector tests
    bit_vector_tests()

    #size=1024*1024
    #mymemobj = getmemobj(size)
    #myint32_tests()
    #myint64_tests()
    #mystr_tests()
    #myint32_aray_tests()
    #myint64_aray_tests()

# verify memory allocated  is all zero
    print(mymemobj)


if __name__ == "__main__":
    main()

