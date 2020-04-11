# Binary Search for a number

def BinarySearch(n,L,start = 0,stop = None):
    ''' Binary Search algorithm

    n - value to find
    L - is a list of values
    start - start index
    stop - stop index

    returns the index of the value in the list, if it is present there,
    and False otherwise'''
    
    if stop == None: # first call of BinarySearch - entire list
        stop = len(L)

    # displaying the part of the list we are working with right now
    print("\n We are working with the following sub-list:\n ", L[start:stop+1])
    
    if start >= stop: # nothing is left and the element wasn't found
        return False

    else:
        middle = (start+stop)//2
        print("middle index = ",middle, "start = ",start,", stop = ",stop,"(in the original list)\n")
        
        if n == L[middle]: # if the element is located
            return middle
        
        elif L[middle] >= n: # if the element is less that the middle element
            # run the Binary Search algorithm on the left half of the current list,
            # including the middle element
            return BinarySearch(n,L,start,middle)
        
        else: # if the element is greater than middle element
            # run the Binary Search algorithm on the left half of the current list,
            # excluding the middle element
            return BinarySearch(n,L,middle+1,stop)

    


def main():

    #nList=[1,2,3,4,5,6,7,8,9,10,12,14,16,18,23,25,27,29,34,36,39,52,56,59,78,79,82,84,85,87,88,89,100,123,145,167]
    nList=[1,7,9,12,17,19,23,45,67,123,167]
    
    print('The list of the numbers:\n',nList)

    n = eval(input('Please, input a value to search for:'))

    index = BinarySearch(n,nList)
    
    if index == False:
        print('%d is not found'%n)
    else:
        print('%d is the %dth element of the list'%(n,index))

main()    
