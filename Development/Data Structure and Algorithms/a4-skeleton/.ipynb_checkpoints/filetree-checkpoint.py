import os
import sys
from stat import *
from mylist import *
from random import randrange
from mystat import *

# cmp function for list lookups
# cmp node objects 
def node_obj_cmp(node, obj):
    if node.nobj == obj:
        return True
    else:
        return False

# compare object names

def node_objname_cmp(node, name):
    if node.nobjname == name:
        return True
    else:
        return False

def node_objid_cmp(node, id):
    if node.nobjid == id:
        return True
    else:
        return False

# file objects 
# mandatory to have these members.
# name - file name (not the full path)
# objid - file object is thisis the inode no. in the stat
# stat - stat object of the file returned by os.stat api.
# dir 0 (default) implies it is not directory but a regular file.
# dir 1 implies it is a directory.
# 

class myfile():

    # look above for argument descriptions.
    # raise exception if dir is 1 and not a dir
    # raise exception fi dir is 0 and not a regular file.
    # DO NOT CHANGE THIS. 
    # you can add additional members if required.

    def __init__(self, objid, name=None, stat=None, dir=0):

        # leave the following in there.
        if name and '/' in name:
            raise Exception("Bad name in file")
        if dir and stat and not S_ISDIR(stat.st_mode):
            s=f'{name} is not a directory'
            raise Exception(s)
        if not dir and stat and not S_ISREG(stat.st_mode):
            s=f'{name} is not a file'
            raise Exception(s)

        self.name=name
        self.objid = objid
        self.stat=stat
        self.dir=dir
        self.path=None
        self.size=None
        self.search=None

    
    # return the file path from root of the tree to which it belongs.
    # eg., I will create a file object with
    # fobj=myfile(241573) ie. only with objectid.
    # print(fobj.path(tree))
    # where this file is part of the tree.  Note: not this instance
    # of the object but the same objectid.
    # it should print the file path.
    # the objectid is found by "ls -i1" in any of the subdirectory
    # of the kernel-0 folder sent to you.  you can do that even on windows
    # with powershell i believe.
    # this function should print the full path of that objectid starting
    # from the kernel-0 folder.
    # eg., if the file kernel-0/mm/f1.c and its objectid is 241573
    # then fobj.file_path(tree) should print kernel-0/mm/f1.c
    # Note: this has to be recalculated from the tree when this function
    # is called. Tree was the object obtained from convert_to tree function
    # at the end of this file.


    def file_path(self, tree):
        self.file_path_helper(tree.root)
        return self.search
    
    def file_path_helper(self,node):
        temp=''
        for children in node.child_list:
            if children.nobj.objid==self.objid:
                self.search=children.nobj.path
            else:
                self.file_path_helper(children)
        
 

    def file_size(self):
        return self.size

    # this is just a helper. feel free to modify the way you want it to help
    # you.

    def __str__(self):
        return f'File Name: {self.name}'

# directory objects inherit from file, uses 
# all of what file has plus some more interfaces.


class mydir(myfile):

    # DO NOT CHANGE THIS.
    # you can add any members below this.

    def __init__(self, objid, name=None, stat=None, ):
        super().__init__(objid, name, stat, 1)
        self.path=None
        self.search=None
        self.total_counter=0
    def __str__(self):
        return f'Folder Name: {self.name}'
    
    
    # find the total no. of files underneath this directory including 
    # the directories (as they are also files) as well. 
    # eg., if you have a folder : kernel-0/mm/f1.c and kernel-0/mm/f2.c
    # dir_total_files of the directory kernel-0 will print : 3. two regular
    # files and one directory file "mm".
    # use case will be :
    # dir=mydir(245173)
    # dir.dir_total_files(tree)
    # where this directory is part of the tree.  Note: not this instance
    # of the object but the same objectid.
    # Note this has to be "calculated" every time the function is called
    # from the passed tree. 
    
    def find_folder(self, tree):
        self.find_folder_helper(tree.root)
        temp=self.search
        self.search=None
        return temp
    
    def find_folder_helper(self,node):
        for children in node.child_list:
            if children.nobj.objid==self.objid:
               # print(children.nobj.path)
               # print('Nodes: ',children.children_count)
                self.search=children
            else:
                self.find_folder_helper(children)
                
                
                
    def dir_total_files(self, tree):
        folder_node=self.find_folder(tree)
        if folder_node!=None:
                self.dir_total_file_helper(tree,folder_node)
                return_counter=self.total_counter
                self.total_counter=0
                return return_counter 

    def dir_total_file_helper(self,tree,node,dir_value=0):
        for children in node.child_list:
            #print(children.children_count,children.nobjname)
            if children.nobj.dir==dir_value:
                self.total_counter+=1
            self.dir_total_file_helper(tree,children,dir_value)
        

    # the below function is similar as above but should print the only the total
    # no. of directories underneath this directory.
    # Note this has to be "calculated" every time the function is called
    # from the passed tree. 

    def dir_total_dirs(self, tree):
        folder_node=self.find_folder(tree)
        if folder_node!=None:
                self.dir_total_file_helper(tree,folder_node,dir_value=1)
                return_counter=self.total_counter+1 # Including the parent itself
                self.total_counter=0
                return return_counter


class mynode():
    # pobj - parent object
    # obj - this object
    # objname - name of this object
    # objid - unique id of this object. for file and dir it is inode numbes.
    # Do not change this.

    def __init__(self, pobj, obj, objname, objid):
        self.child_list=mylist("list")
        self.nobj=obj
        self.nobjname = objname
        self.nobjid=objid
        self.npobj = pobj
        self.children_count=0
        
    def __str__(self):
        if self.npobj==None:
            parent='Root Node'
        else:
            parent=self.npobj.nobj.name
            
        return f'Node : {self.nobjname} Parent : {parent}'  

class mytree():

# init functionf or root object and name and its object id.
# (object id for these objects are all inode numbers).
# Do not change this.

    def __init__(self, obj, root_name, id):
        self.root=mynode(None, obj, root_name, id)
        self.total_nodes=1
        self.root.path='kernel-0'

# the following two functions are helper functions for 
# constructing the tree, insertions etc..



# Lookup objname from a parent node, if found return
# node object. 
# If it does not  exist, create a node for that objname,
# objid combinations, ensure to add it to the appropriate child
# list.

    def lookup_create(self, pobj:mynode, objname, objid, obj):
        lookup_result=self.lookup(pobj,objname)
        if lookup_result==None:
            obj_node=mynode(pobj,obj,objname,objid)
            pobj.child_list.add(obj_node)
            self.total_nodes+=1
            pobj.children_count+=1
            return obj_node
        else:
            return lookup_result 
            

# Lookup objname from a parent node, if found return
# node object. If not, return None.

    def lookup(self, pobj:mynode, objname):
        child_list=pobj.child_list
        for child in child_list:
            if child.nobjname==objname:
                return child
          
    def print_tree(self,root):
        print(f'{root.nobj.name} Child: ', end="")
        for i in root.child_list:
            print(f'{i.nobj.name}, ', end="")
        print('\n')
        for i in root.child_list:
            self.print_tree(i) 


# Method on the tree object to traverse and it will call the function
# func with the passed arguments (variable argument args), for 
# every line of the object it will generate as output corresponding 
# to the input file in function convert_input_to_tree().
#
# for the eg. mentioned in the comments of that function
# the function func() will get called for each of the
# lines given there. And that string will be passed as first argument to the
# function.

# func_traverse(tree, test_func, argobj) returned by convert_input_to_tree() will call 
# test_func(fobj, "kernel-0", argobj) where fobj is the mydir obj for kernel-0.
# test_func(fobj, "kernel-0/arch", argobj) where fobj is the mydir obj for kernel-0/arch.
# test_func(fobj, "kernel-0/arch/boot", argobj) where fobj is the mydir obj for kernel-0/arch/boot.
# test_func(fobj, "kernel-0/arch/boot/bootloader.lds", argobj) where fobj is the  myfile obj 
# for kernel-0/arch/boot/bootloader.lds.

# you can test this function by putting the string in some file or std output
# and then compare the entire output with the original input file (sort both to
# avoid any ordering issues).

    def func_traverse(self, func, *args):
        mylist=args[0]
        mylist.append('kernel-0')
        self.func_traverse_helper(func,self.root,mylist)
        

# exactly same as above function except that the traversal starts
# from an intermediary mynode() object ie., an interior node.

    def func_node_traverse(self, node, func, *args):
        #YOUR CODE
        raise NotImplementedError
        pass

# some debug stuff may be useful.
    def func_traverse_helper(self,func, node,args):
        for child in node.child_list:
            func(child.nobj,child.nobj.path,args)
        for child in node.child_list:
            self.func_traverse_helper(func,child,args)
        
        
    def dump1(self, root):
        print(root.obj)
        print(f'{root.obj} Child: ', end="")
        for i in root.child_list:
            print(f'{i.obj}, ', end="")
        print('\n')
        for i in root.child_list:
            self.dump1(i)

# some debug stuff may be useful.

    def dump(self):
        print(f'Total Nodes: {self.total_nodes}')
        self.dump1(self.root)


# Function takes an input file name 
# and converts that into an object instance of 
# the tree class as defined above.
# you can only use the operations given above to construct the tree.
# no other functions should be added.
# input file will be of the form:
#kernel-0
#kernel-0/arch
#kernel-0/arch/alpha
#kernel-0/arch/alpha/boot
#kernel-0/arch/alpha/boot/bootloader.lds
# the above should be converted to tree with root object being the
# directory object - kernel-0, and there are arch, alpha and boot as
# directory objects below and bootloader.lds as a file object below.
# construct the appropriate hierarchy. The mynode.obj should be 
# either a mydir or myfile object as defined above.

# returns "tree" object.

# hint use readlines, strip, and split if required  and os.stat


def convert_input_to_tree(filename):
    file_object=open(filename,'r')
    root=file_object.readline()
    root=root.strip()
    root_stats=mystat(root)
    #Create a dir object for root node
    root_dir=mydir(root_stats.st_ino,root,root_stats)
    #Creating a filetree with the root
    filetree=mytree(root_dir,root,root_stats)
    
    # Now that the tree is created with a root node, we have to iterate through the paths
    # and add new nodes if it doesn't exist.
    # Read the lines in file one by one
    read_line=file_object.readline()
    while(len(read_line)>0):
        read_line=read_line.strip()
        path_list=read_line.split('/')
        path_list=path_list[1:] # Excluding the root element as it has already been added
        # Now set the parent node as the root node and start walking through the path 
        parent_node=filetree.root
        path='kernel-0'
        for location in path_list:
            path+='/'+location # Create the path to be used later
            #Check if the node to be added is a file or a dierctory
            stats=mystat(path)
            directory=S_ISDIR(stats.st_mode)
            # If directory create a di object.Else create a file object
            current_node=None
            if directory:
                current_node=mydir(stats.st_ino,location,stats)
                current_node.path=path
            else:
                current_node=myfile(stats.st_ino,location,stats)
                current_node.path=path
            #Check if the node exists or not. 
            parent_node=filetree.lookup_create(parent_node,location,stats.st_ino,current_node)
           # print(path)
            
           # print(parent_node.nobjname,'Parent Name')
            # Now that we have identified the node to be added, 
            # Check if it already exist in the parent node            
            
       # print('\n\n')


        read_line=file_object.readline()
    return filetree
