# To draw a calculator

import graphics
from graphics import *

# Button Class

class Button:

    def __init__(self,win,center,width,height,label):
        w, h =width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin = x - w
        self.xmax = x + w
        self.ymin = y - h
        self.ymax = y + h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

        self.deactivate()    

    def clicked(self, pt):
        x = pt.getX()
        y = pt.getY()
        return (self.active and
                self.xmin <= x <= self.xmax and
                self.ymin <= y <= self.ymax)

    
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True


    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False



def calculator():
    win = GraphWin("Calculator",600,700)
    win.setCoords(0,0,6,7)
    win.setBackground("slategray")
    
    # IGNORE FOR NOW.
    bSpecs = [ (2,1,'0'), (3,1,'.'),
               (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
               (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
               (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C') ]

    for (x,y,label) in bSpecs:
        draw_calc_key(win,x,y,label)

def draw_calc_key(win,x,y,label):
    Button(win,Point(x,y),0.75,0.75,label)



    
    
