import numpy
import random


def sortwithloops(input):
      y = len(input)
      x = range(len(input))
      for i in x:
        for j in range(1, y-i):
            if input[j-1] > input[j]:
             (input[j-1], input[j]) = (input[j], input[j-1])
      return input

def sortwithoutloops(input):
    return sorted(input)


def sortwithnumpy(input):
      return numpy.sort(input)
        

def searchwithloops(input, value):

    while value in input:
        return "true"
    else:
        return "false"

          
def searchwithoutloops(input, value):
  
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

    L= random.sample(range(0,200),100)

    print sortwithloops(L) 
    print "               "
    print sortwithoutloops(L)
    print "               "
    print sortwithnumpy(L)
    print "               "
    print searchwithloops(L, 5) 
    print searchwithloops(L, 202) 
    print searchwithoutloops(L, 5) 
    print searchwithoutloops(L, 202) 
    print searchwithnumpy(L,5) 
    print searchwithnumpy(L,202)


import timeit


setup = '''
import numpy
import copy
import random

input = random.sample(range(0,200),100)
def sortwithloops(input):
      y = len(input)
      x = range(len(input))
      for i in x:
        for j in range(1, y-i):
            if input[j-1] > input[j]:
             (input[j-1], input[j]) = (input[j], input[j-1])
      return input

def sortwithoutloops(input):
    return sorted(input)


def sortnumpy(input):
      return numpy.sort(input)
        

def searchwithloops(input, value):

    while value in input:
        return "true"
    else:
        return "false"

          
def searchwithoutloops(input, value):
  
    if value in input:
        return "true"
    else:
        return "false"


def searchwithnumpy(input, value):
	val = numpy.asarray(input)
	if value in val:
		return True
	else:
		return False    
'''

print " n = 1000 "
n=1000
t = timeit.Timer("x= copy.copy(input);sortwithloops(x)",setup)
print " Sort with loops (n=1000)  : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy(input);sortwithoutloops(x)",setup)
print " Sortwithoutloops (n=1000) : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy(input);sortnumpy(x)",setup)
print " Sortwithnumpy  (n=1000)   : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy(input);searchwithloops(x,3)",setup)
print " Searchwithloops (n=1000)  : ",  t.timeit(n)


t = timeit.Timer("x= copy.copy(input);searchwithoutloops(x,3)",setup)
print " Searchwithoutloop (n=1000): ",  t.timeit(n)

t = timeit.Timer("x= copy.copy((input));searchwithnumpy(x,3)",setup)
print " Searchwithnumpy  (n=1000) : ",  t.timeit(n)

print "                          "

print " n = 10000"
n=10000
t = timeit.Timer("x= copy.copy(input);sortwithloops(x)",setup)
print " Sort with loops  (n=10000)  : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy(input);sortwithoutloops(x)",setup)
print " Sortwithoutloops (n=10000)  : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy(input);sortnumpy(x)",setup)
print " Sortwithnumpy  (n=10000)    : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy(input);searchwithloops(x,3)",setup)
print " Searchwithloops (n=10000)   : ",  t.timeit(n)


t = timeit.Timer("x= copy.copy(input);searchwithoutloops(x,3)",setup)
print " Searchwithoutloop(n=10000)  : ",  t.timeit(n)

t = timeit.Timer("x= copy.copy((input));searchwithnumpy(x,3)",setup)
print " Searchwithnumpy (n=10000)   : ",  t.timeit(n)


