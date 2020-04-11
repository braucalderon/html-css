# Ch 4 Problem 11

import graphics
from graphics import *


def main():
    win=GraphWin('House', 400, 400) # window appears
    win.setCoords(0.0, 0.0, 40, 40,) # (0.0 X left, 0.0 Y top,
    #40, X right, 40, Y bottom coords)
 
   
    #make the main house wall
    p1=win.getMouse()
    p2=win.getMouse()
    rect=Rectangle(p1,p2)
    rect=Rectangle(Point(35,15), Point(5,00))
    rect.setOutline('black')
    rect.draw(win)

    #door
    p3=win.getMouse()
    door=Rectangle(p3,p3)
    door=Rectangle(Point(15,10), Point(10,00))
    door.setOutline('black')
    door.draw(win)

    p4=win.getMouse()
    window=Rectangle(p4,p4)
    window=Rectangle(Point(29,13), Point(26,10))
    window.setOutline('black')
    window.draw(win)

    p5=win.getMouse()
    roof=Line(p5,p5)
    roof=Line(Point(35,15),Point(20,35))
 
    roof.setOutline('black')
    roof.draw(win)
    
    #left line
    #p5=win.getMouse()
    roof1=Line(p5,p5)
    roof1=Line(Point(5,15), Point(20,35))
    roof1.setOutline('black')
    roof1.draw(win)
    
    
    
    

main()
