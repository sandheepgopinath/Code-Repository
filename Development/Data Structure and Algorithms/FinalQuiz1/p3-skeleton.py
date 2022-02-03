
# node_bitmaps is an array of strings from 0.. n-1
# nodes are named from 0 till n-1. (ie. N nodes)
# 
# Each string in the array represents the edges
# of the node "index" to all other nodes in hexa
# decimal format.
# ie. if node_bitmaps[0]=7f
# node 0 has edges to node 2,3,4,5,6,7.
# 
# You can assume no. of nodes is aligned to multiples of 4.
# 
# if node_bitmaps[3]=8a
# it has edges to  node 0, node 4 and node 6.
# 8 is 1000 and a is 1010 

# RETURN: this computes the total length across the nodes.
# if two nodes v0 and v1 has an edge, then the length between
# the two nodes is 1.
# if there is a path between the v(i) and v(j), then the
# length (i,j) = count of the no. of edges  in the shortest path
# between i and j.

# If there is no path between i and j  length(i,j) = 321*n
# where n is the no. of nodes.
# The length() function below calculates the sum of all
# lengths between all possible nodes calculated the above way.

# eg., for a three nodes:
# node_bitmaps[2,

# INPUT: node_bitmaps is a string where each string is a hexadecimal
# representation of connectivity between the nodes.

def length(node_bitmaps)

    #YOUR CODE
    raise NotImplementedError

