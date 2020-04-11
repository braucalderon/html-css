#Ismael Garrido CSI 32
#fibonacci.py
#This program computes the N fibonacci number for a non-negative integer.


def FibRec(n):
    if n < 0:
        raise ValueError("Cannot compute fibonacci sequence of negative numbers")
   
    elif not isinstance(n,int):
        raise ValueError('n should be integer')
    
    print("Computing the fibonacci sequence of n = "+ str(n))
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return FibRec( n-1) + FibRec(n-2)

def main():
    print("This program computes the N fibonacci number for a non-negative integer")
    while True:
        n = int(input("Please enter an integer to compute its fibonacci number: "))
        Fib = FibRec(n)
        print("Fibonacci of %d = %d"%(n,Fib))

main()


