from LList import *
from random import *



def main():

    n = int(input("Enter a list of number: "))

    L = LList()

    for i in range(1,n+1):
        L.append(i)

    L=[i for i in range (n) ]
    print(L)
        




main()

    

    
