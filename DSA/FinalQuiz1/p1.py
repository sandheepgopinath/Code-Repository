
# in a complete binary tree -- 
# complete binary tree is one where all the levels
# are full except for the leaf level where also the nodes
# are all left bound.
# bfslist has the bfs traversal nodes.
# return the inorder traversal nodes.


def inorder_from_bfs(bfslist):
    out=[]
    position=0
    inorder_helper(position,bfslist,out)
    return(out)

added=[]

def inorder_helper(position,l,out):
    if position<len(l):
        inorder_helper((2*position)+1,l,out)
        out.append(l[position])
        inorder_helper((2*position)+2,l,out)