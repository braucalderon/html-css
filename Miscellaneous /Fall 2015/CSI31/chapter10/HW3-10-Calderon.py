# CH 10, Problem # 10


from math import *

class Cube:

    def __init__(self, length):
        self.length = length
        self.surface = (6*(length**2))
        self.volume = (length**3)

    def getsurfaceArea(self):
        return self.surface

    def getVolume(self):
        return self.volume


def main():

    length = float(input("Enter the length pls: "))

    
    sqr=Cube(length)
    
    
    print ('The surface of the cube is:  ',sqr.getsurfaceArea())
    print ('The volume of the cube is:   ',sqr.getVolume())
    

main()
    
                            
                            
        
        

