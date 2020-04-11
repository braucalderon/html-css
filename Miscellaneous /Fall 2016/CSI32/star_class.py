from cs1graphics import *
from math import *

class Star(Polygon):
    ''' Star graphics object

        constructor requires the following optional parameters
        numRays         number of rays, 5 by default
        outerRadius     outerRadius of the star, 30 by default
        innerRario      ratio of inner radius to outer radius, 0.5 by default
        center          where to place the star, Point(30,30) by default '''
    
    def __init__(self,numRays=5,outerRadius=30,innerRatio=0.5,center=Point(30,30)):
        """ constructor of Star class

        numRays - number of rays
        outerRadius - outer radius
        innerRatio = inner radius / outer radius
        center - point where to display the object in the Canvas

        """
        
        Polygon.__init__(self) # call the parent's class constructor
        
        top = Point(0,-outerRadius) # top point of the star
        #print("Top point:",top)
        angle = 360.0/(2*numRays) # angle between points
        #print("Angle:",angle)

        for i in range(numRays):
            self.addPoint(top^(angle*2*i)) # adding ray point
            #print(i+1,'th ray point:',top^(angle*i))
            self.addPoint(innerRatio*top^(angle*(2*i+1))) # adding inner point
            #print(i+1,'th inner point:',top^(angle*(i+0.5)))
            
        #moving Reference Point from the top point to the center of the star
        self.adjustReference(0,outerRadius)

        #moving the star to the given by the user point (as the center of the star)
        self.moveTo(center.getX(),center.getY())
        
        #record the inner ratio as attribute
        self._innerRatio=innerRatio 

    def setInnerRatio(self,newRatio):
        ''' allows to change the innerRatio '''
        
        factor=newRatio/self._innerRatio
        self._innerRatio=newRatio

        #we will modify only inner points: 1st, 3rd, 5th, ...
        for i in range(1,self.getNumberOfPoints(),2):
            self.setPoint(factor*self.getPoint(i),i)

def main():
    paper=Canvas(800,600,'lightyellow','Stars')

    s=Star()
    paper.add(s)

    tt= Text("Click anywhere to continue ...",12,Point(400,550))
    paper.add(tt)

    paper.wait()
    
    s.setInnerRatio(0.2)

    s1=Star(8,40,0.3,Point(200,200))
    s1.setBorderColor('dark blue')
    s1.setFillColor('blue')

    paper.add(s1)

    tt.setMessage("That's it! Click anywhere to quit.")

    paper.wait()

    paper.close()
    

main()    
        
        
        

