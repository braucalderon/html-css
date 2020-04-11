from graphics import *

def square():    

    win = GraphWin('f', 300, 300)
    shape = Rectangle(Point(80,80), Point(10,10))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
 
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)

square()
