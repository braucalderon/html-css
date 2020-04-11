
import graphics
from graphics import *

class FunnyButton:

    def __init__(self, win, center, width, height, label):
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin = x - w
        self.xmax = x + w
        self.ymin = y - h
        self.ymax = y + h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.setOutline('red')
        self.label = Text(center, label)
        self.label.setFill('black')
        
        self.rect.draw(win)
        self.label.draw(win)
        
        self.deactivate()
        

    def clicked(self, pt):
        x = pt.getX()
        y = pt.getY()
        return (#self.active and
                self.xmin <= x <= self.xmax and
                self.ymin <= y <= self.ymax)

    def activate(self):
        self.label.setFill('black')
        self.rect.setFill('lightgray')
        
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('blue')
        self.rect.setFill('blue')
        self.rect.setWidth(1)
        self.active = False












def main():

     
     win = GraphWin("Tic Tac Toe", 400, 400)
     win.setCoords(0, 0, 100, 100)
     
     button=FunnyButton(win,Point(50,10), 40, 20, "Click here to change my color")
     button.activate()
 #   pt=win.getMouse()
##   button.deactivate()
     button1=FunnyButton(win,Point(50,30), 40, 20, "Second button to chnage")
     button1.activate()
     button2=FunnyButton(win,Point(50,60), 40, 20, "third button")
     button2.activate()
     button3=FunnyButton(win,Point(50, 80), 40, 20, "Fourth button")
     button3.activate()
     pt=win.getMouse()
