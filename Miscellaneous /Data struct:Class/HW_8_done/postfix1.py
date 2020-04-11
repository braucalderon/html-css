# postfix1.py
# HW 8
# Exercises 3

from Stack import Stack

def postfix(n):

    s=Stack()
    n1 = n.split()
    n2 = len(n1)

    for i in range(n2):
        if n1[i].isdigit():
            s.push(int(n1[i]))

        elif n1[i] == "+":
            a = s.pop()
            b = s.pop()
            s.push(int(a)+int(b))

        elif n1[i] == "-":
            a = s.pop()
            b = s.pop()
            s.push(int(a)-int(b))

        elif n1[i] == "*":
            a = s.pop()
            b = s.pop()
            s.push(int(a)*int(b))

        elif n1[i] == "^":
            a = s.pop()
            b = s.pop()
            s.push(int(a)**int(b))

        elif n1[i] == "/":
            a = s.pop()
            b = s.pop()
            s.push(int(a) / int(b))

    return s.pop()

def main():

    n=input("Enter a valid posfix notation: ")
    t = postfix(n)

    print(t)


main()
            
    
    
