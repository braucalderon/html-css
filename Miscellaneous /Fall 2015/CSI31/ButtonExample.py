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
##        self.line=nonsenseline
##        self.nonsenseline = line( Point(self.xmin, self.ymin), Point(self.xmax, self.ymax) )
##        self.nonsenseline.draw(win)

        
        self.deactivate()
        

##    def lineX(self, line):
##        self.line=line
##        
##        self.line = Text( Point(self.xmin, self.ymin), Point(self.xmax, self.ymax) )
##        self.line.draw(win)
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

##    def fillRed(self):
##        self.rect.setFill('red')

    
        



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
     
 #    color = 'blue'
     color = 'orange'
     while True:
 #        color = 'orange'
         while color == 'orange':
         
             pt=win.getMouse()
             if button.clicked(pt) and button.active:
                 button.deactivate()
                 button.line.draw(color)
             if button1.clicked(pt) and button1.active:
                 button1.deactivate()
                 button1.line.draw(color)
    ##             elif button.rect.setFill(color) != button1.rect.setFill(color1):
    ##                 button1.re
             if button2.clicked(pt) and button2.active:

                 button2.deactivate()
                 button2.rect.setFill(color)
             if button3.clicked(pt) and button3.active:
                 button3.deactivate()
                 button3.rect.setFill(color)
             color = 'blue'
         while color == 'blue':
             pt=win.getMouse()
             if button.clicked(pt) and button.active:
                 button.deactivate()
                 button.rect.setFill(color)
             if button1.clicked(pt) and button1.active:
                 button1.deactivate()
                 button1.rect.setFill(color)
    ##             elif button.rect.setFill(color) != button1.rect.setFill(color1):
    ##                 button1.re
             if button2.clicked(pt) and button2.active:

                 button2.deactivate()
                 button2.rect.setFill(color)
             if button3.clicked(pt) and button3.active:
                 button3.deactivate()
                 button3.rect.setFill(color)
             color="orange"
             
             

         

    
##     win = GraphWin("This button will change...I hope", 400, 400)
##     win.setCoords(0, 0, 100, 100)
     
##     example=FunnyButton(win,Point(50,50), 60, 30, "Click here to change the button")
##     example.activate()

main()
'''
win = GraphWin("Tic Tac Toe", 400, 400)
win.setCoords(0, 0, 100, 100)
a=Circle(50,10)

a=Circle(Point(50,50),10)
a.draw(win)
a.setFill('red')
b=Circle(Point(50,50),8)
b.setFill('white')
b.draw(win)   
'''
