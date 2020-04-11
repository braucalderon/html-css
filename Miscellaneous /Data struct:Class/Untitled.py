#array.py


from array import *

def main():

    array1 = array('l', [1,2,3,4,5,6,7,8,9] )

    print(array1)
    print(array1.itemsize)

    array1.append(10)
    print ("Adding: ", array1)

    array1.pop()
    print("Remove: ", array1)

    array1.insert(1, 6)
    print("Insert: ",array1)

    print(array1.buffer_info())
    array1.reverse()
    print(array1)

    print(1,2,3,3,4,4,5,6,7,7)
    n=set([1,2,3,3,4,4,5,6,7,7])
    print("Removing duplicates using 'set': ",n)
    

    


main()
