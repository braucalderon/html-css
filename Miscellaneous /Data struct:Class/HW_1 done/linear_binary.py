# This programs has implementation of two algorithms:
# linear search and binary search ...

from time import time


def linear_search(items,target):

    
    i = 0
    while i < len(items):
        if items[i] == target:
            return i
        i += 1
    return -1
  


def binary_search(items,target):

    low = 0
    
    high = len(items) - 1
    
    while low <= high:
        mid = (low + high) // 2
        item = items[mid]
        if target == item :
            return mid
        elif target < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():

    
    
    numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999
    #print(numbers)

    start = time()
    linear_search(numbers, 10)
    end = time()
    print("Linear search, 10")
    print("Start time:",start)
    print("End time:",end)
    print("Total time to run the numbers: ",end-start,"\n")
    

    
    start = time()
    linear_search(numbers,499999)
    end = time()
    print ("Linear search, 499999")
    print ("Start time:",start)
    print ("End time:",end)
    print ("Total time to run the numbers: ",end-start,"\n")

    start = time()
    linear_search(numbers,999999)
    end = time()
    print("Linear search, 999999")
    print ("Start time:",start)
    print ("End time:",end)
    print ("Total time to run the numbers: ",end-start,"\n")


    start = time()
    binary_search(numbers, 10)
    end = time()
    print("Binary search, 10")
    print ("Start time:",start)
    print("End time:",end)
    print("Total time to run the numbers: ",end-start,"\n")

    
    start = time()
    binary_search(numbers,499999)
    end = time()
    print ("Binary search, 499999")
    print ("Start time:",start)
    print ("End time:",end)
    print ("Total time to run the numbers: ",end-start,"\n")

    start = time()
    binary_search(numbers,999999)
    end = time()
    print ("Binary search, 999999")
    print ("Start time:",start)
    print ("End time:",end)
    print ("Total time to run the numbers: ",end-start,"\n")

"""
RUNNIN TIME

T(n): 6n + 42

Theta(n)=Theta(n)
"""
main()  




  



