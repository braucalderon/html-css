# postfix.py
# HW_8
# Exercise 3

from Stack import *


def postfix(n1):

    s=Stack()

    t= n1.split()    
    for p in t:
        if p.isdigit(): # check for integers in the list 
            s.push(int(p)) # append the ints into Stack(self.items)

        else:
            s1 = s.pop()
            s2 = s.pop() # goes first 
            print(s2)
            final = result(p,s2,s1) # the order matters (s2 goes first becasue s2 pop up first)
            s.push(final)
            
            
    return s.pop()

def result(p1,s2,s1):

    if p1 == "^":
        return (s1 ** s2)

    if p1 == "*":
        return (s1 * s2)

    if p1 == "+":
        return (s1 + s2)

    if p1 == "/":
        return (s1 / s2)

    if p1 == "-":
        return (s1 - s2)


print("Space is required to solve between the numbers and operations")
n=input("Enter a valid Postfix Noation: ")
n1=postfix(n)
print("Postfix evaluation is: ", n1)






