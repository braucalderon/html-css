class Thing:
    
    def __init__(self):
        self._a = 1 # original values
        self._b = 4
    
    def foo(self, param): 
        self._a = self._a + param # add original value + the value of print(it.foo())
        self._b = self._b + param # Ex: self._a=1 + print(it.foo(1)) = self._a=2
        return (self._a + self._b) # add new both values from print(it.foo())
    
    def bar(self, param): # add the value of print(it.bar()) 
        a = self._a + param #if value is 0 added into def foo()
        b = self._b + param
        return (a + b) # sum the values without saving the values into __init__
    
    def __str__(self):# give the values from def foo()
        return 'a is '+str(self._a)+', b is '+str(self._b) 

def main():

    it = Thing()
    print (it.foo(3))
    print (it.bar(0))
    print(it)
  


main()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
