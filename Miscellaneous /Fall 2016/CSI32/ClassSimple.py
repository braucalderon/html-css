class Sneetch:
    
    def __init__(self):
        self._a = 3
        self._b = 4

    def x(self):
        print (self._a)

    def y(self):
        print (self._b)

class StarBellySneetch(Sneetch):

    def __init__(self):
        Sneetch. __init__(self)
        self._b = 7
        self._c = 8

    def y(self):
        print (self._b, self._c)

    def z(self):
        print (self._a, self._c)

def main():

    alice=Sneetch()
    bob=StarBellySneetch()

    print(bob.y())
     
   

main()

