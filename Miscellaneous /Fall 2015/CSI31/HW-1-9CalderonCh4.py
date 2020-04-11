import graphics
from graphics import *
import math

def main():
    win=GraphWin('Rectangle Segment', 400, 250)
    win.setCoords(0.0,0.0,4.0,4.0)
    Text(Point(1.8,3.7), "Horizontal line first followed by a vertical line").draw(win)
    Text(Point(1.9,3.3), "with another horizontal line and vertical line to finish the rectangle").draw(win)

    #Get and draw four vertices of a rectangle
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)
    p4=win.getMouse()
    p4.draw(win)

    #Use Polygon object to draw the triangle
    rectangle=Polygon(p1,p2,p3,p4)
    rectangle.setFill('white')
    rectangle.setOutline('red')
    rectangle.draw(win)

 
    #dx=(p1.getX() + p2.getX())+(p3.getX()+p4.getX())
    width=(p1.getY()+p4.getY())+(p2.getY()+p3.getY())
    length=(2*width)
    perimeter = (2*(length + width))
    area=(float(length*width))

    print ('The area of the rectangle is:', area)
    print ('The perimeter of the rectangle is:', perimeter)

main()
