# Page 38, Ex: 9

"""
Write a specification and implementation for a function that squeezes
the duplicates out of  a sorted list.

 
________________________________________


Implementation

def squeeze_n():

    new=[]
    for i in range(len()-1):
        if i =! [i+1]:
            added to the list(new)
            (i) + 1
    append(last element added)
    numbers[:] = new  add new list & slices and delete them
            


Theta notiation

Theta(n) = T(n)

Theta efficiency
T(n) = 3n + 5

________________________________________

Reference of n[:] =  new

http://effbot.org/zone/python-list.htm


"""






def squeeze_n(n):

    """Remove duplicates by comparing the values

    Pre-condition: sort the numerical values
    Post-Condition: with the sorted numerical values removes the duplicates """

 
    new=[]
    for i in range(len(n)-1):
        if n[i] != n[i+1]:      # compare if the element is not equal to the next element
            new.append(n[i])    # append it if it is not equal
            i += 1
    new.append(n[i])        # last element added 
    n[:] = new              # assign individual items or slices and to delete them                      

""" n = new throws the original list, I did a little more of research about n[:]=new
I thought it was assigning to a new list as well but different style, but it has  another
fuctionality in the program"""


    
n=[1,1,3,3,3,4,5,5,8,9,9,9,9,10]
print("Original list:",n)

squeeze_n(n)
print("List without duplicates:",n)

