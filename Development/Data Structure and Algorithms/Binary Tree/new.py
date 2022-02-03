import os
import sys
from stat import *
from mylist import *
from random import randrange
from filetree import *

# different comparison functions for the 
# file objects.
# object equality of myfile objects is based on objectid
# which is the inode number

def myfile_cmp(obj1, obj2):
    if obj1.objid == obj2.objid:
        return True
    return False

# size based comparison between two myfile objects

def myfile_size_cmp(obj1, obj2):
    if obj1.file_size() == obj2.file_size():
        return 0
    if obj1.file_size() < obj2.file_size():
        return -1
    if obj1.file_size() > obj2.file_size():
        return 1

# size comparison but val is "int" and obj is myfile object.

def myfile_val_cmp(val, obj):
    if val == obj.file_size():
        return 0
    if val < obj.file_size():
        return -1
    if val > obj.file_size():
        return 1


# return a list of sorted objects only by using the public functions of 
# the binary tree.
# the methods given below. No internal members are seen by this.
# use any of the methods defined in the tree as given below. No new methods
# can be added for this.

def sorted_bintree(tree):
    return tree.traverse()


# binary node
# with left and right child

class mybnode(mynode):
    # pnode - parent node
    # obj - this object
    # left and right and obj add the way you want
    # Do not change this.
    # you can add more members if you want

    def __init__(self, pnode, obj):
        self.left=None
        self.right=None
        self.pnode = pnode
        self.obj_list=mylist('list') #Creating a list to store duplicate values of same size
        if obj!=None:
            self.obj_list.add(obj)  # Adding the first object to the list
        
    def first(self):
        element=None
        for element in self.obj_list:
             pass
        return element       

#mybintree class. 
# it stores objects of myfile . but it can be general.
# objcmp, objvalcmp, and valcmp are the functions
# for checking. see the comparison functions above.
# objcmp -- for comparing two object ids returns true if
# they are equal.
# objvalcmp(obj1, obj2) -- for comparing value of two objects 
# returns 0, -1 or 1. 0 if equal, -1 if obj1 < obj2, and 
# 1 if obj1 > obj2. 
# valcmp(val, obj)--. compares val (in this case it represents 
# the size ) with object value.


class mybintree():

# init functionf or root object and name and its object id.
# (object id for these objects are all inode numbers).
# Do not change this.

    def __init__(self, obj):
        self.root=mybnode(None, obj)
        self.total_nodes=1
        self.list_objects=mylist('list')
        self.tree_height=0
        self.node_count=0
        self.leq_count=0
        self.present=False
        self.eq_node=None
# insert object into the binary tree. objcmp and objvalcmp corresponds to the
# definitions listed above.
# if the same object is trying to get  inserted twice, raise exception
# ensure all the objects from the file list kernel-0.files are inserted
# here appropriately.
# 

    def insert(self, obj, objcmp, objvalcmp):
        if self.root.first()==None:
            self.root=mybnode(None,obj)
        else:
            if self.search_tree(obj,objcmp,objvalcmp):
                raise Exception('Element already present')
            else:
                self.insert_helper(self.root,obj,objcmp,objvalcmp) # Calling the helper function for insertion
        
    def insert_helper(self,node,obj,objcmp,objvalcmp):
        if objvalcmp(node.first(),obj)<0:
            if node.left!=None:
                self.insert_helper(node.left,obj,objcmp,objvalcmp)
            else:
                #print('Inserting left node')
                new_node=mybnode(node,obj)
                new_node.pobj=node
                node.left=new_node
                self.total_nodes+=1
        elif objvalcmp(node.first(),obj)>0:
            if node.right!=None:
                self.insert_helper(node.right,obj,objcmp,objvalcmp)
            else:
                #print('Inserting right node')
                new_node=mybnode(node,obj)
                new_node.pobj=node
                node.right=new_node
                self.total_nodes+=1
        elif objvalcmp(node.first(),obj)==0:
                #print(node.first().name)
                node.obj_list.add(obj)  
                #print(node.obj_list)          
                
    def dump1(self,node):
        if node!=None:
            print('Parent',node.obj_list.first().size)
            if (node.left!=None):
                print('Left:',[i.size for i in node.left.obj_list],end=' ')
            if (node.right!=None):
                print('Right:',[i.size for i in node.right.obj_list])
            print('\n')
            self.dump1(node.left)
            self.dump1(node.right)
        
            
        
# Function to search for an object in a binary tree. If found, it will return True, 
# Else it will return false
# If the value of obj is 1, it will try to find the matching object
# Else it will try to find the matching value

    def search_tree(self,element,objcmp,objvalcmp):
        self.search_tree_helper(self.root,element,objcmp,objvalcmp)
        temp=self.present
        self.present=False
        return temp

    def search_tree_helper(self,node,element,objcmp,objvalcmp):
        """Compare the objects if dir is 1 and compare the values inside
            objects if dir is 0"""
        if node!=None:           
            if objvalcmp(node.first(),element)==0:
                if objcmp(node.first(),element):
                    self.present=True
                    return True
                    raise StopIteration
            elif objvalcmp(node.first(),element)<0:
                self.search_tree_helper(node.left,element,objcmp,objvalcmp)
            elif objvalcmp(node.first(),element)>0:
                self.search_tree_helper(node.right,element,objcmp,objvalcmp)

                    
# traverse the binary tree func is the passed function has to be invoked with
# the object and the variable args *args passed here.

    def traverse(self, func=None, *args):
        '''Pre Order traversal'''        
        self.traverse_helper(self.root)
        temp=self.list_objects
        self.list_objects=mylist('list')
        return temp

    def traverse_helper(self,node):
        if node!=None:
            self.traverse_helper(node.right)
            for element in node.obj_list:
                self.list_objects.add(element)
            self.traverse_helper(node.left)

    def travers_from_node(node, func, *args):
        #YOUR CODE
        raise NotImplementedError

# returns the height of the binary tree

# returns the count of the binary tree nodes.
    
    
    def height(self):
        return(self.height_helper(self.root)-1)
         
    def height_helper(self,node):
        if node==None:
            return 0
        lHeight=self.height_helper(node.left)
        rHeight=self.height_helper(node.right)
        maxHeight=lHeight
        if rHeight>maxHeight:
            maxHeight=rHeight
        return maxHeight+1

    def count(self):
        '''pre order traversal'''
        self.node_count=0
        self.count_helper(self.root)
        return self.node_count
    
    def count_from_node(self,node):
        self.node_count=0
        self.count_from_node_helper(node)
        return self.node_count

    
    def count_from_node_helper(self,node):
        if node!=None:
            self.node_count+=node.obj_list.size
            self.count_helper(node.left)
            self.count_helper(node.right)

    def count_helper(self,node):
        if node!=None:
            self.node_count+=node.obj_list.size
            self.count_helper(node.left)
            self.count_helper(node.right)



# returns the count of the binary tree nodes less than or equal to val.
# Note: This cannot use the traverse function has to calculate from the
# current tree by going through it. cannot use any other public functions.

    def count_leq(self, val, valcmp):
        self.leq_count=0
        node_value=self.countleq_helper(self.root,val,valcmp)
        return node_value
    

    def countleq_helper(self,node,val,valcmp):

        if node==None:
            return 0

    
        if valcmp(val,node.first())<0:
            return self.countleq_helper(node.left,val,valcmp)
        elif valcmp(val,node.first())>0:
            self.leq_count+=self.count_from_node(node.left)
            self.leq_count+=node.obj_list.size
            return self.countleq_helper(node.right,val,valcmp)
        elif valcmp(val,node.first())==0:
            self.leq_count+=self.count_from_node(node.left)
            self.leq_count+=node.obj_list.size
            return self.leq_count
           

# returns the count of the binary tree nodes greater than or equal to val.
# Note: This cannot use the traverse function has to calculate from the
# current tree by going through it. cannot use any other public functions.

    def count_geq(self, val, valcmp):
        #YOUR CODE
        raise NotImplementedError


# returns the count of the binary tree nodes equal to val.
# Note: This cannot use the traverse function has to calculate from the
# current tree by going through it. cannot use any other public functions.

    def count_eq(self, val, valcmp):
        self.eq_node=None
        self.count_eq_helper(self.root,val,valcmp)
        return self.eq_node.obj_list.size

    def count_eq_helper(self,node,val,valcmp):
        if node!=None:           
            if valcmp(val,node.first())==0:
                self.eq_node=node
                return node
                raise StopIteration
            elif valcmp(val,node.first())<0:
                self.count_eq_helper(node.left,val,valcmp)
            elif valcmp(val,node.first())>0:
                self.count_eq_helper(node.right,val,valcmp)

