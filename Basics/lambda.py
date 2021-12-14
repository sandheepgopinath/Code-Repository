"""
 Python function to print pascals triangle using lambda function
 Author : Sandheep Gopinath
 TimeStamp : 20 September 2021, 14:35

"""

appendZero=lambda x: x.append(0)
appendStartZero=lambda x: x.insert(0,0)
newLayer=lambda emptyList,newList: [emptyList.append(newList[i]+newList[i+1]) for i in range(len(newList)-1)]
initialize=lambda x : x.append([0,1,0])

def pascalsList(numberOfLayers):
	""" Create a list of element for Pascals triangle. 
	    This list has to be printed using a pretty print function or else
            it would appear just like a list of lists"""
	pTriangle=[]
	initialize(pTriangle)
	lastLayer=pTriangle[0]
	for i in range(numberOfLayers):
		temp=lastLayer
		emptyList=[]
		newLayer(emptyList,temp)
		appendStartZero(emptyList)
		appendZero(emptyList)
		lastLayer=emptyList
		pTriangle.append(lastLayer)
	return pTriangle

print(pascalsList(10))
