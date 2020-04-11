#this file contains definition of the BinaryNumber class
# unfinished

# check numbers 0011 and 101
# 0011 < 101, but the program will report that it is not so

def binary_number_check(s):

    check=True
    
    for ch in s:
        if ch != '1' and ch != '0':
            check = False
            break

    return check

class BinaryNumber:

    def __init__(self, s):
        ''' constructor of class BinaryNumber '''

        if binary_number_check(s) == False:
            print("! Warning !: ",s,"is not a binary string")

        self._bn = s

    def __str__(self):
        ''' print method '''

        if binary_number_check(self._bn) == True:
            return self._bn
        else:
            return "not a binary string"

    def __lt__(self,other):
        ''' less than, i.e. is b1<b2 ? '''

        n1=len(self._bn)
        n2=len(other._bn)

        if n1==n2: # if the lengths of the binary strings are equal, then
            # we can compare the using lexicographical order
            # Lexicographical comparison of binary strings works well on
            # the strings of the same length, and doesn't work on strings
            # of different length, for example:
            # >>> '101' > '11'
            # False
            # but it is True
            return self._bn < other._bn
            
        elif n1 < n2: # if the length of the first binary number is less
            # than the length of the second binary number, then the first
            # binary number is less then the second one
            # check out this case: 0011 and 101, the verdict given by program is wrong
            return True
            
        else:# if the length of the first binary number is greater
            # than the length of the second binary number, then the first
            # binary number is greater then the second one, not less
            return False

    def __eq__(self,other):
        ''' equal: is b1=b2 ? '''

        # check out 0011 and 11. These numbers are equal but the program will
        # report otherwise
        return self._bn == other._bn

    def __gt__(self, other):

        n1=len(self._bn)
        n2=len(other._bn)

        if n1 > n2:
            return True
        else:
            return False

    def __or__(self,other):

        n1=len(self._bn)
        n2=len(other._bn)

        if n1 == n2:
            for i 

    def __int__(self):
        ''' conversion to decimal number system '''

        # reverse the order of the elements in the binary string
        # why do we need it? - see what addednds does the loop generate
        
        bn_rev = self._bn[::-1]

        n=len(self._bn)

        result=0 # the result of conversion

        for i in range(n):
            result += int(bn_rev[i])*2**i

        return result

    def __add__(self,other):  
        ''' addition of two binary numbers '''

        # reverse the order of the elements in both binary strings
        # same question as before: why do we need it?
        # answer: it is easier to start adding first elements,
        # corresponding second elements and so forth
        b1_rev=self._bn[::-1]
        b2_rev=other._bn[::-1]

        # take the lengths of the strings, and then work with the maximum
        n1 = len(b1_rev)
        n2 = len(b2_rev)
        n = max(n1,n2)
        
        result = str() # the resulting binary string is initially an empty string
        c_o = 0 # carry over digit

        for i in range(n):
            #print "interation ",i
            #print n1,",",n2
            if i >= n1:
                t=int(b2_rev[i])+c_o
                result += str(t%2)
                #print "Case1:"
                #print result
                c_o = t//2
                #print c_o
            elif i >= n2:
                t=int(b1_rev[i])+c_o
                result += str(t%2)
                #print "Case2:"
                #print result
                c_o = t//2
                #print c_o
            else:
                t=int(b1_rev[i])+ int(b2_rev[i])+c_o
                result += str(t%2)
                #print "Case3:"
                #print result
                c_o = t//2
                #print c_o

        # take care of the case, when an extra character needs to be added to the
        # result, i.e. the resulting binary string is longer that the original strings
        if c_o != 0:
            result += str(c_o)

        return BinaryNumber(result[::-1]) # method returns a Binary Number, not binary string
    

def main():
    str1 = input("Please, input a binary string (it should consist of 0's and 1's only:")

    b1=BinaryNumber(str1)

    str2 = input("Please, input another binary string (it should consist of 0's and 1's only:")

    b2=BinaryNumber(str2)

    print("Here are our binary numbers: ", b1, " and ", b2)

    print(b1,"<", b2," ? ", b1<b2)
    print(b1,"=", b2," ? ", b1==b2)
    print(b1,">", b2," ? ", b1>b2)

    print("Decimal form of",b1, "is", int(b1))

    print(b1," + ",b2," = ", b1+b2)
    
main()    
        
