# in-class work:
# Use LList.py and write a program that will do the following:
# 1) create a linked list for the sequence $[1,...n]$,
#    where value for $n$ is given by the user.
# 2) insert three numbers (your choice), provided by the user into the list 
#    (your choice of positions, but they should be different) 
# 3) Delete two numbers from the list (also your choice for the
#     different positions)
# 4) Find the sum of all values in the linked list.
#


from LList import *
from random import randint

def F():
    n=eval(input("Please enter a positive integer between 6 and 100:"))

    # one way of creating a linked list on N elements
    # using list comprehension to create a list on N elements from 1 to N
    #L=[i for i in range(1,n+1)]
    #print(L) # printing the list
    #myList=LList(L) # creating a linked list with N elements from 1 to N

    # another alternative of creating a linked list is this one:
    myList=LList()
    for i in range(1,n+1):
        myList.append(i)

    # printing the elements of the linked list
    for i in range(n):
            print(myList[i])

    print("Inserting items...")

    myList.insert(n%2,100)
    myList.insert(n-2,109)
    myList.insert(2,121)

    # printing the elements of the linked list
    for i in range(n):
            print(myList[i])

    print("Deleting some items....")
    myList.pop(randint(0,n))
    myList.pop(randint(0,n))

    # printing the elements of the linked list
    for i in range(n):
            print(myList[i])

    # adding up all the values in the linked list
    s=0
    for i in myList:
            s+=i
    print("The sum of all the values from the list is ",s)


F()
