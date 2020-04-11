#Finobbacci1


def BinarySearch(n,p,start = 0,stop = None):
    ''' Binary Search algorithm

    n - value to find
    L - is a list of values
    start - start index
    stop - stop index

    returns the index of the value in the list, if it is present there,
    and False otherwise'''
    
    if stop == None: # first call of BinarySearch - entire list
        stop = len(p)

        
    if start >= stop: # nothing is left and the element wasn't found
        return False

    else:
        middle = (start+stop)//2
        #print("middle index = ",middle, "start = ",start,", stop = ",stop,"(in the original list)\n")
        
        if n == p[middle]: # if the element is located
            return middle
        
        elif p[middle] >= n: 
            return BinarySearch(n,p,start,middle)
        
        else: 
            return BinarySearch(n,p,middle+1,stop)




n=eval(input('Enter a non-negative number to find the Finobacci sequence: '))

def main(n):
 

    if n == 1 or n == 2:
        return 1
    return main(n-1) + main(n-2)

p=[]
for i in range(1,(n+1),n):
        
    p.append(main(i))
    print(p)

print('\nThe Finobbaci series of',n, 'is: ', p)


index = BinarySearch(n,p)

if index == False:
    print ('\nThe %dth Fibonacci number could not be found on the list as an element.' %n)
else:
    print('\nThe %dth Fibonacci number is the %dth element of the list.'%(n,index))


             

main(n)
            



