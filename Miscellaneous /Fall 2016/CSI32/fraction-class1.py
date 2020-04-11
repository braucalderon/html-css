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
        """ constructor of Fraction class takes two optional parameters: numerator and denominator """
        
        if d==0: # fraction is undefined
            self._n=0
            self._d=0
        else : # reducing to lowest terms
            factor = gcd(abs(n),abs(d)) # getting GCD of numerator and denominator
            self._n=int(n/factor)
            self._d=int(d/factor)

    def __str__(self):
        """ prints fraction """
        if self._d == 0: # if denominator is 0
            return 'Undefined'
        elif self._d ==1 : # if denominator is 1, then it is an integer
            return str(self._n)
        else:
            return str(self._n) + '/' + str(self._d)


def main():

    f1=Fraction(10,14)
    f2=Fraction(4,16)

    print("We have two fractions:", f1, "and", f2)

main()
