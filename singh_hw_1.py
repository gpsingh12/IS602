#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions

import numpy
import timeit
def sortwithloops(input):
      """ Function sorts the list from the input values using .
    Arg:
        input(list):list of integers is the input value
    Return:
        returns the sorted list.
    Example:
    >>> sortwithloops([5,3,6,3,13,5,6])
    >>> [3, 3, 5, 5, 6, 6, 13]
    """
      y = len(input)
      x = range(len(input))
      for i in x:
        for j in range(1, y-i):
            if input[j-1] > input[j]:
             (input[j-1], input[j]) = (input[j], input[j-1])
      return input

def sortnumpy(input):
      return numpy.sort(input)

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop

        
def sortwithoutloops(input):
    """Function takesinput as list and sort the list using builtin function.
    Arg:
        input(list): the input value is list of integers
    Return:
        returns the sorted list
    Example:
    >>>sortwithoutloops([5,3,6,3,13,5,6])
    >>>[3, 3, 5, 5, 6, 6, 13]
    """
    return sorted(input) #return a value

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions

def searchwithloops(input, value):
    """Function search for a value in the input and return True or False.
    Arg:
        input(list): the input value is list of integers
        value(num): uses a numerical value to search in the list.

    Return:
         returns True or Flase if value is in the list or not
    Example:
    >>>searchwithloops([5,3,6,3,13,5,6], 3)
    >>>True
    >>>searchwithloops([5,3,6,3,13,5,6], 4)
    >>>False
    """
    while value in input:
        return "true"
    else:
        return "false"

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop            
    
def searchwithoutloops(input, value):
    """Function search for a value in the input and return True or False without
        using the loops.
    Arg:
        input(list): the input value is list of integers
        value(num): uses a numerical value to search in the list.

    Return:
         returns True or Flase if value is in the list or not
    Example:
    >>>searchwithloops([5,3,6,3,13,5,6], 3)
    >>>True
    >>>searchwithloops([5,3,6,3,13,5,6], 4)
    >>>False
    """
    if value in input:
        return "true"
    else:
        return "false"
def searchwithnumpy(input, value):
	input = numpy.asarray(input)
	if value in input:
		return True
	else:
		return False    


if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]
    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortnumpy(L) 
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
    print searchwithnumpy(L,5) #True
    print searchwithnumpy(L,11)#False
    setup1 = "from __main__ import searchwithloops"
    setup2 = "from __main__ import searchwithnumpy"
    print timeit.timeit("searchwithloops(input,5)",setup1)
    print timeit.timeit("searchwithnumpy(input,5)",setup2)
    
