# Midterm
# Question 8

from LList import *

def main():
    
    l = LList([10,4,3,1])
    print("The normal list: ")
    for item in l:
        print(item, end= ' ')
    l.reverse()
    print("the resersed list: ")
    for item in l:
        print(item, end=" ")
    
main()
