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

class MixedNumber():

        def __init__(self,w=0,num=0,denom=1): # initially, by default, we have 0 0/1 
                self._w = w
                if num >= denom: # if fractional part is improper fraction, fix it
                        self._w += num//denom
                num = num%denom
                self._f=Fraction(num,denom)
                # we need to fix the improper fraction when a negative number 
      

        def __str__(self):
                if self._w == 0:
                        return str(self._f)
                else:
                        return str(self._w) + '  ' + str(self._f)

      # conversion of a mixed number to improper fraction
        def mixed2fraction(self):
                """ conversion of a mixed number to improper fraction """
               
                return Fraction(self._w,1) + self._f

        def __add__(self,other): # Addition of two mixed numbers or
                             #a mixed number and a fraction
                a=self.mixed2fraction()
                #print(self, '    is ', a)

                if isinstance(other,MixedNumber):
                        b=other.mixed2fraction()
                        #print(other, '    is ', b)
                        c=a+b

                elif isinstance(other,Fraction):
                        c=a+other

                elif isinstance(other,int):
                        b=Fraction(other,1)
                        c=a+b
                else:
                        print('Tried to perform the following operation:',self,' + ',other)
                        raiseTypeError('These items cannot be added')

                return fraction2mixed(c)

        def __sub__(self,other): # Subtraction of two fractions

                a=self.mixed2fraction()

                if isinstance(other, MixedNumber):
                        b=other.mixed2fraction()
                        c = a-b
                        return mixed2fraction(c)
                
                else:
                        print('It is not a fraction')
                                    
                

        def __mul__(self,other): # Multiplication of two fractions
                
                a=self.mixed2fraction()

                if isinstance(other, MixedNumber):
                        b=other.mixed2fraction()
                        c = a*b
                        return mixed2fraction(c)
                else:
                        print('It is not a fraction')
                        

        def __truediv__(self,other): # division of two mixed numbers
                a=self.mixed2fraction()
                #print(self, '    is ', a)
                
                if isinstance(other,MixedNumber):
                        b=other.mixed2fraction()
                        #print(other, '    is ', b)
                        c=a/b

                elif isinstance(other,Fraction):
                        c=a/other

                elif isinstance(other,int):
                        b=Fraction(other,1)
                        c=a/b

                else:
                        print('Tried to perform the following operation:',self,' / ',other)
                        raiseTypeError('These items cannot be added')

                return fraction2mixed(c)

        def __neg__(self): # negation of a fraction

                
                return -self
                 

        
def main():
        m1=MixedNumber(2,5,4)
        m2=MixedNumber(1,2,3)
        print("Created m1 = ",m1)
        print("Created m2 = ",m2)
        f1=m1.mixed2fraction()
        print("coverting ", m1, " to improper fraction: ", f1)
        f2=m2.mixed2fraction()
        print("converting ",m2, " to improper fraction: ", f2)

        f3=Fraction(14,23)
        print("created fraction f3 = ",f3)
        m3=fraction2mixed(f3)
        print("converting fraction", f3, " to a mixed number: ", m3)

        f4 = Fraction(23,12)
        m4=fraction2mixed(f4)
        print("Coverting fraction ", f4, " to a mixed number: ", m4)

        input("Press Enter to continue ...")

        print("Adding two mixed numbers:")
        m4=m1+m2
        print(m1, " + ", m2, " = ",m4)

        print("Adding a mixed number and a fraction:")
        m5 = m1 + f3
        print(m1, " + ", f3, " = ", m5)

        input('Press Enter to continue')

        print("Adding a mixed number and an integer:")
        m6 = m1+2
        print(m1, " + ", 2, " = ",m6)

        input('Press Enter to continue')

        print("Dividing a mixed number by a mixed number:")
        m7=m1/m2
        print(m1, " / ", m2, " = ", m7)

        input('Press Enter to continue')

        print("Dividing a mixed number by 2:")
        m8 = m1/2
        print(m1, " / 2 = ", m8)

        input('Press Enter to continue')

        f5 = m1.mixed2fraction()
        f6 = m2.mixed2fraction()
        
        print('\nSubtraction of Improper fractions: ')
        print(f5,"-", f6, "=",f5.__sub__(f6))

        input('Press enter to continue')

        print('\nMultiplication of Improper fractions:', )
        print(f5, "*", f6, "=", f5.__mul__(f6))
        

        input('Press enter to continue')

        
        print('\nNegation of Improper fractions: ' )
        print(f5.__neg__(),',', f6.__neg__())
        

        
    

main()    
        
