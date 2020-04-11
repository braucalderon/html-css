from math import *
from fraction_class_lib import *

def fraction2mixed(f):
        """
        conversion of a fraction to a mixed number
        
        so far if a user tries to convert a proper fraction to a mixed number,
        the warning is displayed, but the mixed number is still created,
        with 0 as the whole part (quotient)
        """
        
        n=f.getNum()
        d=f.getDen()
        
        if n < d:
            print("Warning: you tried to convert a proper fraction to a mixed number!")
            print("The mixed number was created, but its whole part (quotient) is 0")
            return MixedNumber(0,n,d)
        else:
            return MixedNumber(n//d,n%d,d)

class MixedNumber(Fraction):
        """ Mixed number class

        self._q:  quotient (whole part)
        self._d:  denominator
        self._n:  numerator
        """
        # customizing constructor for Mixed Number class
        def __init__(self,quotient=0,num=0,denom=1): # initially, by default, we have 0 0/1
                ''' constructor '''

                self._q = quotient

                if num < denom: # fractional part is a proper fraction
                        Fraction.__init__(self,num,denom)
                else: # takes care of improper fraction as a fractional part of the mixed number              
                        self._q += num // denom
                        r=num%denom
                        Fraction.__init__(self,r,denom)

        def __str__(self):
                ''' display '''
                if self._d == 0: # if denominator is 0, the mixed number is undefined
                        return 'Undefined'

                elif self._n == 0: # if the numerator is 0
                        if self._q == 0: # and the whole part(quotient) is 0
                                return str(0)

                        else: # and the whole part (quotient) is not 0
                                return str(self._q)
        
                else: # 2 3/4
                        return str(self._q) + ' ' + str(self._n) + '/' + str(self._d)
            

      
        def mixed2fraction(self):
                """ conversion of a mixed number to improper fraction """
                return Fraction(self._q*self._d+self._n,self._d)

        def __add__(self,other): # Addition of two numbers
                ''' addition of two mixed numbers done through addition of two fractions '''
                a = self.mixed2fraction()
                #print(self, '    is ', a)

                if isinstance(other,MixedNumber):
                    b = other.mixed2fraction()
                    #print(other, '    is ', b)
                    c = a + b

                elif isinstance(other,Fraction):
                    c = a + other

                elif isinstance(other,int):
                    b = Fraction(other,1)
                    c = a + b

                else:
                    print('Tried to perform the following operation:',self,' + ',other)
                    raiseTypeError('These items cannot be added')

                return fraction2mixed(c)

        def __sub__(self,other): # Subtraction of two numbers
                pass

        def __mul__(self,other): # Multiplication of two numbers
                pass

        def __truediv__(self,other): # division of two numbers

                a=self.mixed2fraction()
                
                #print(self, '    is ', a)
                
                if isinstance(other,MixedNumber):
                        b = other.mixed2fraction()
                        #print(other, '    is ', b)
                        c = a/b

                elif isinstance(other,Fraction):
                        c = a/other

                elif isinstance(other,int):
                        print("Dividing by integer")
                        b = Fraction(other,1)
                        c = a/b
                else:
                        print('Tried to perform the following operation:',self,' / ',other)
                        raiseTypeError('These items cannot be added')

                return fraction2mixed(c)

        def __pow__(self,n): # exponent
                pass

        def __neg__(self): # negation of a mixed number
                pass

def main():
        m1=MixedNumber(2,5,4)
        m2=MixedNumber(1,2,3)
        print("Created m1 = ",m1)
        print("Created m2 = ",m2)
        f1=m1.mixed2fraction()
        print("converting ", m1, " to improper fraction: ", f1)
        f2=m2.mixed2fraction()
        print("converting ",m2, " to improper fraction: ", f2, "\n")

        f3=Fraction(14,23)
        print("created fraction f3 = ",f3)
        m3=fraction2mixed(f3)
        print("converting fraction", f3, " to a mixed number: ", m3, "\n")

        f4 = Fraction(23,12)
        m4=fraction2mixed(f4)
        print("Converting fraction ", f4, " to a mixed number: ", m4, "\n")

        input("Press Enter to continue ...")

        print("Adding two mixed numbers:")
        m4=m1+m2
        print(m1, " + ", m2, " = ",m4, "\n")

        print("Adding a mixed number and a fraction:")
        m5 = m1 + f3
        print(m1, " + ", f3, " = ", m5, "\n")

        input('Press Enter to continue')

        print("Adding a mixed number and an integer:")
        m6 = m1+2
        print(m1, " + ", 2, " = ",m6, "\n")

        input('Press Enter to continue')

        print("Dividing a mixed number by a mixed number:")
        m7=m1/m2
        print(m1, " / ", m2, " = ", m7, "\n")

        input('Press Enter to continue')

        print("Dividing a mixed number by 2:")
        m8 = m1/2
        print(m1, " / 2 = ", m8)

        print("\nThat's it!")
    

main()    
        
