# The set is a list of integers.
# do a special ordering of the elements of the set
# in such a way:
# absolute_difference(set[i]-set[i+1]) < absolute_difference(set[i+2]-set[i+1])
# return a list of the special ordered elements that
# satisfies the above property.

# RETURN: set of ordered elements that satisfies the above property.
# INPUT: "set" is a list.
def bubble_sort(l):
    end_pointer=len(l)-1
    for i in range(end_pointer,-1,-1):
        for j in range(0,i):
            if l[j]>=l[j+1]:
                temp=l[j]                                                     
                l[j]=l[j+1]
                l[j+1]=temp
    return l

def create_set(l):
    unique=[]
    for element in l:
        if element not in unique:
            unique.append(element)
    return bubble_sort(unique)




def  special_order(set):
    l=bubble_sort(set)
    output=[]

    for i in range(len(l)):
        j=len(l)-1-i
        if i<j:
            output.append(l[i])
            output.append(l[j])
            
    # Reversing the order
    out=[]
    for i in range(len(output)-1,-1,-1):
        out.append(output[i])
    return out
