# a strange object moves in the graphics window

from cs1graphics import *
import time
from random import *

def main():
    
    # instantiaing a canvas (graphics window)
    paper=Canvas(600,600,(218,240,248),"Flying/jumping Object")

    time.sleep(1) # waiting

    #paper.setBackgroundColor((245,226,245))

    # Define 8 points for the "star"
    a=Point(100,250)
    b=Point(200,200)
    c=Point(250,100)
    d=Point(300,200)
    e=Point(400,250)
    f=Point(300,300)
    g=Point(250,400)
    h=Point(200,300)
    obj=Polygon(a,b,c,d,e,f,g,h) # instantiating a polygon
    obj.setFillColor((245,226,245)) # filling the polygon

    paper.add(obj) # adding to the canvas
    
    for i in range(40): # 40 moves
        # getting a random number from (-50,50) for change in x
        x=randrange(-50,50)
        # getting a random number from (-50,50) for change in y
        y=randrange(-50,50) 
        paper.remove(obj) # removing the previous drawing of the "star"
        obj.move(x,y) # moving the "star" 
        paper.add(obj) # shoing it (at its new position)
        time.sleep(0.25) # waiting
         

main()    
