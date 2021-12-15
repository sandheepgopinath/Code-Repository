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

def main():
    n = len(sys.argv)
    #print(f'argument list {n} {sys.argv}')
    if n < 2: 
        usage(sys.argv)
    filename=sys.argv[1]
    tree=convert_input_to_tree(filename)

    # ensure output matches properly
    # change the object id below properly to match your system
    # see testcase3.txt description.

    d=mydir(2415723)
    print(f' total files in dir: {d.dir_total_files(tree)}')


if __name__ == "__main__":
    main()
