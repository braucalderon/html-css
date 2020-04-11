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
        else : # reducing to lowest terms, keeping negative sign in demonimator
            factor = gcd(abs(n),abs(d)) # getting GCD of numerator and denominator
            self._n=int(n/factor)
            self._d=int(d/factor)
            if self._d < 0: # this is to keep the sign in denominator
                self._n = - self._n
                self._d = - self._d

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

    def __neg__(self):
        """ negation of a fraction """
        return Fraction(-self._n,self._d)

    def n_invert(self):
        """ negative reciprocal of a fraction """
        return Fraction(self._d,self._n).__neg__()
        #return -Fraction(self._d,self._n)

    def getNum(self):
        """ returns numerator of the fraction """
        return self._n

    def getDen(self):
        """ returns denominator of the fraction """
        return self._d
    
