import graphics
from graphics import *

def shapes():

    win = GraphWin("Practice6",100,100)
    win.setCoords(0,0,10,10)
    Cr = Circle(Point(5,5),4)
    Cr.draw(win)
    Rt = Rectangle(Point(5,5),Point(6,7))
    Rt.draw(win)
