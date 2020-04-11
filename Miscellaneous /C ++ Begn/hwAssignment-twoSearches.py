# This programs has implementation of two algorithms:
# linear search and binary search ...

from time import time

def main():

  numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999
  print(numbers)

  start = time()
  linear_search(numbers,10)
  end = time()

  print the resulting time with comments

  start = time()
  linear_search(numbers,499999)
  end = time()

  print the resulting time with comments

  start = time()
  linear_search(numbers,999999)
  end = time()

  print the resulting time with comments

  do the same for binary search

  

  

def linear_search(items,target):
  """ add the specification here """
  
  .......

  return index or return -1


def binary search(items,target):
  """ add the specification here """
  
  if len(items) == 0:
    return False

  else:
    midpoint = len(items) // 2
    if target == items[midpoint]:
      return midpoint
    
    elif items[midpoint] >= target:
      
        return binary_search.index(items,target,midpoint)

    else:
        return binary_search.index(items,target, midpoint+1)
      
  

  .....

  return index or return -1
