#Input is two string lists 
#Return the values which are present in both lists as a list of strings
def intersectionOfTwoLists(x, y):
	return list(set(x) & set(y))
	

#Input is two string lists 
#Return the values which are present in list 1 but not in the list 2 as a list of strings	
def differenceOfListOneToListTwo(x,y):
	return list(set(x) - set(y))
	

#Input is two string lists 
#Return the values which are present in list 2 but not in the list 1 as a list of strings	
def differenceOfListTwoToListOne(x,y):
	return list(set(y) - set(x))
	

#Input is two string lists 
#Return the values which are present in one list but not in the other list irrespective of list order as a list of strings	
def differenceOfTwoLists(x,y):
	return unionOfTwoLists(list((set(x) - set(y))) , list((set(y) - set(x))))
	
	
#Input is two lists
#Return the union of two lists
def unionOfTwoLists(x,y): 
	return list(set().union(x,y)) #We can add any number of lists inside the union function to combine all the lists
	
