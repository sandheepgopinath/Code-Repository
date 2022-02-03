import os
import sys
from stat import *
from mylist import *
from random import randrange

from inspect import currentframe, getframeinfo

from filetree import *

def usage(arg):
    print(f'usage: {arg[0]}: <filename>')
    sys.exit(1)

# please test this .. untested code.

# obj is the actual object mydir or myfile object
# objpath is a string.
# *args is the same argument I passed from main function.
# in this case tlist.

def list_files(obj, objpath, *args):
    tlist=args[0]
    tlist.append(objpath)

def main():
    n = len(sys.argv)
    #print(f'argument list {n} {sys.argv}')
    if n < 2: 
        usage(sys.argv)
    filename=sys.argv[1]
    tree=convert_input_to_tree(filename)
    tlist=[]
    tree.func_traverse(list_files, tlist)
    for i in tlist:
            print(i)

if __name__ == "__main__":
    main()
