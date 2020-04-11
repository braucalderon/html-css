class One:
    def __init__(self,a,b=1):
        self._n=a
        self._g=b

    def n(self, a,b):
        self._n*=a
        self._g+=b
        return self._n + self._g

    def g(self):
        return self.n(2,3)

m=One(3)
print(m.g())
print(m.n(2,1))


##class MyClass:
##
##    def __init__(self,l):
##        self._l=l
##
##    def thing(self):
##        m=0
##        for item in self._l:
##            if item > 0:
##                m += item**2
##        return m
##
##def main():
##
##    a = MyClass([1,2,3,4,-1,-2,-3,-4])
##    b = a.thing()
##    print('b=',b)
##
##main()

