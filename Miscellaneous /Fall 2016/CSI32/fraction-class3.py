from math import *

def gcd(a,b):
    """ gcd(value,value) -> value

    Finds Greatest Commond Divisor of two integers, a and b,
    using Euclid's method"""
    u, v = a, b

    counter2=0;
    while v != 0:
        r = u % v
        u = v
        v = r
        counter2 +=1

    return u

class Fraction:
    ''' Fraction(numerator = 0,denominator = 1) ->  numerator / denominator'''

    def __init__(self, n = 0, d = 1):
        """ constructor of Fraction class takes two optional parameters:
            numerator and denominator """
        
        if d==0: # fraction is undefined
            self._n=0
            self._d=0
        else : # reducing to lowest terms
            factor = gcd(abs(n),abs(d)) # getting GCD of numerator and denominator
            self._n=int(n/factor)
            self._d=int(d/factor)
            
        if d < 0 and n > 0:# here the change 
            self._n =+ (self._n *-1)
        if n < 0 and d > 0:
            self._d =+ (self._d *-1)

    def __str__(self):
        """ prints fraction """
        if self._d == 0: # if denominator is 0
            return 'Undefined'
        elif self._d ==1 : # if denominator is 1, then it is an integer
            return str(self._n)
        else:
            return str(self._n) + '/' + str(self._d)


    def __add__(self,other):
        """ Addition two fractions """
        return Fraction(self._n*other._d+other._n*self._d,self._d*other._d)

    def __sub__(self,other):
        """ Subtraction of two fractions """
        return Fraction(self._n*other._d-other._n*self._d,self._d*other._d)

    def __mul__(self,other):
        """ Multiplication of two fractions """
        return Fraction(self._n*other._n,self._d*other._d)

    def __truediv__(self,other):
        """ division of two fractions self/other """
        return Fraction(self._n*other._d,self._d*other._n)

    def __pow__(self,n):
        """ Raise a fraction to power n """
        return Fraction(pow(self._n,n),pow(self._d,n))
    
    
        
    
def main():

    f1=Fraction(10,14)
    f2=Fraction(4,16)

    print("We have two fractions:", f1, "and", f2)

    print("The sum:", f1, "+", f2, "=", f1+f2)

    print("Their difference:", f1, "-", f2, "=", f1-f2)

    print("Their product:", f1, "*", f2, "=", f1*f2)

    print("Their quotient:", f1, "/", f2, "=", f1/f2)

    print(f1, "to the power " + str(2) + "=", f1**2)

    # testing when the program doesn't work properly

    f3 = Fraction(-1,2)
    f4 = Fraction(2,-3)

    print("The sum:", f3, "+", f4, "=", f3+f4) # - looks weird

    f3 = Fraction(-1,2)
    f4 = Fraction(-2,-3)

    print("The sum:", f3, "+", f4, "=", f3+f4) # - looks weird

    f3 = Fraction(-1,2)
    f4 = Fraction(2,3)

    print("The sum:", f3, "+", f4, "=", f3+f4) # - looks weird 

    

        
main()
