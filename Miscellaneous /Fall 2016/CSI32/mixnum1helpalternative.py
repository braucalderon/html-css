# mixnum.py
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
        if abs(n) < d:
            print("Warning: you tried to convert a proper fraction to a mixed number!")
            print("The mixed number was created, but its whole part (quotient) is 0")
            return MixedNumber(0,n,d)
        if abs(n)> abs(d) and n<0:
                return MixedNumber(-(abs(n)//abs(d)),abs(n)%abs(d),d)
        
        else:
            return MixedNumber(n//d,n%d,d)

class MixedNumber():

        def __init__(self,w=0,num=0,denom=1): # initially, by default, we have 0 0/1 
                self._w = w
                if num >= denom: # if fractional part is improper fraction, fix it
                        self._w += num//denom
                num = num%denom
                self._f=Fraction(num,denom)
      

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

        def __sub__(self,other): # Subtraction of two mixed numbers or
                                # a mixed number and a fractions
            a=self.mixed2fraction()
            print(self, '    is ', a)

            if isinstance(other,MixedNumber):
                b=other.mixed2fraction()
                c=a-b
            elif isinstance(other,Fraction):
                c=a-other

            elif isinstance(other,int):
                b=Fraction(other,1)
                c=a-b
            else:
                print('Tried to perform the following operation:',self,' + ',other)
                raiseTypeError('These items cannot be added')
            return fraction2mixed(c)


        def __mul__(self,other): # Multiplication of two fractions
            
            a=self.mixed2fraction()
            
            
            if isinstance(other,MixedNumber):
                    b=other.mixed2fraction()
                    
                    c=a*b

            elif isinstance(other,Fraction):
                    c=a*other

            elif isinstance(other,int):
                    b=Fraction(other,1)
                    c=a*b

            else:
                    print('Tried to perform the following operation:',self,' / ',other)
                    raiseTypeError('These items cannot be added')

            return fraction2mixed(c)

        def __truediv__(self,other): # division of two mixed numbers
                a=self.mixed2fraction()
               
                
                if isinstance(other,MixedNumber):
                        b=other.mixed2fraction()
                        
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
        

        def __neg__(self):# negation of a mixedNumber
                if isinstance(self,MixedNumber):
                        c = -self.mixed2fraction()
                return fraction2mixed(c)
                
                
                if isinstance(self,Fraction):
                        if self < 0:
                                return abs(self)
                        else:
                                return (-1)*self
                return fraction2mixed(c)
                        
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
        
        print("Substracting two mixed number:")
        m9 = m1- m2
        print(m1, " - ", m2, " = ", m9)

        input('Press Enter to continue')

        print("Substracting a mixed number and a fraction:")
        m10 = m1 - f4
        print(m1, " - ", f4, " = ", m10)

        input('Press Enter to continue')

        print("Substracting a mixed number and an integer")
        m11 = m1 - 2
        print(m1, " - ", 2, " = ", m11)

        input('Press Enter to continue')

        print("Multiplying a mixed number by a mixed number:")
        m12 = m1 * m2
        print(m1, " * ", m2, " = ", m12)

        input('Press Enter to continue')

        print("Multiplying a mixed number by 4:")
        m13 = m2 * 4
        print(m2, " * ", 4, " = ", m13)

        input('Press Enter to continue')

        print("Negation of a fractionm")
        m14= -m1
       
        
        print(m14, "is the negation of",m1)
        
        

main()
"""Created m1 =  3  1/4
Created m2 =  1  2/3
coverting  3  1/4  to improper fraction:  13/4
converting  1  2/3  to improper fraction:  5/3
created fraction f3 =  14/23
Warning: you tried to convert a proper fraction to a mixed number!
The mixed number was created, but its whole part (quotient) is 0
converting fraction 14/23  to a mixed number:  14/23
Coverting fraction  23/12  to a mixed number:  1  11/12
Press Enter to continue ...
Adding two mixed numbers:
3  1/4  +  1  2/3  =  4  11/12
Adding a mixed number and a fraction:
3  1/4  +  14/23  =  3  79/92
Press Enter to continue
Adding a mixed number and an integer:
3  1/4  +  2  =  5  1/4
Press Enter to continue
Dividing a mixed number by a mixed number:
3  1/4  /  1  2/3  =  1  19/20
Press Enter to continue
Dividing a mixed number by 2:
3  1/4  / 2 =  1  5/8
Press Enter to continue
Substracting two mixed number:
3  1/4     is  13/4
3  1/4  -  1  2/3  =  1  7/12
Press Enter to continue
Substracting a mixed number and a fraction:
3  1/4     is  13/4
3  1/4  -  23/12  =  1  1/3
Press Enter to continue
Substracting a mixed number and an integer
3  1/4     is  13/4
3  1/4  -  2  =  1  1/4
Press Enter to continue
Multiplying a mixed number by a mixed number:
3  1/4  *  1  2/3  =  5  5/12
Press Enter to continue
Multiplying a mixed number by 4:
1  2/3  *  4  =  6  2/3
Press Enter to continue
Negation of a fractionm
-3  1/4 is the negation of 3  1/4 """

