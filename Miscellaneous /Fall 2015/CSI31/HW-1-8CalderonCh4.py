import graphics
from graphics import *
import math 

def main():
    win=GraphWin('Line Segment', 400, 400)
    win.setCoords(0.0,0.0,3.0,3.0)
    Text(Point(1.5,2.7), "Draw a line segment").draw(win)
    Text(Point(1.5,2.4), "Click the mouse one time to start the point\n"
         "of the line segment and click the second time for the end of it").draw(win)
    
    
    #to get the line segment with the Mouse
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)

    #the line being draw
    line=Line(p1,p2)
    line.setOutline('cyan')
    line.draw(win)

    #formulas
    #dx=x2-x1
    #dy=y2-y1

    
    dx=p2.getX()-p1.getX()
    dy=p2.getY()-p1.getY()
    slope= dy/dx

    lengh=math.sqrt(dx**2+dy**2)

    print('slope:', slope)
    print('lengh:', lengh)
    
    
    
    
   
main()
