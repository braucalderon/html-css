# Program that uses Button class to count

import graphics
from graphics import *
import random
from random import *

# Button Class

class Button:
    "This creates a nice Button"

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
        "Tests a point"
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


def main():
    win = GraphWin("testwindow", 400, 400)
    win.setCoords(0,0,100,100)
    count_button = Button(win,Point(50,20),60,20,"Click Me!")
    reset_button = Button(win,Point(20, 80),35, 20,"Reset")
    quit_button = Button(win,Point(80,80),30,20,"Quit")

    count_button.activate()
    reset_button.activate()
    quit_button.activate()
    
    value = ord("0")
    number = Text(Point(50,50),chr(value))
    number.draw(win)
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if count_button.clicked(pt):
            value = value + 1
            number.setText(chr(value))

        if value == ord("9"):
            count_button.deactivate()

        if reset_button.clicked(pt):
             value = ord("0")
             number.setText(chr(value))
             count_button.activate()

    


        pt = win.getMouse()


    win.close()

def ThreeButtonMonty():
    win = GraphWin("testwindow", 400, 400)
    win.setCoords(0,0,100,100)
    door1 = Button(win,Point(20,80),20,20,"Door 1")
    door2 = Button(win,Point(50, 80),20, 20,"Door 2")
    door3 = Button(win,Point(80,80),20,20,"Door 3")

    door1.activate()
    door2.activate()
    door3.activate()

    instr_text = Text(Point(50,20),"Click a door")
    instr_text.draw(win)


    prize = randrange(1,4)
    
    pt = win.getMouse()
    hasWon = False
    
    if door1.clicked(pt) and prize == 1:
        hasWon = True

    if door2.clicked(pt) and prize == 2:
        hasWon = True       

    if door3.clicked(pt) and prize == 3:
        hasWon = True


    if hasWon:
        instr_text.setText("You Won!")
    else:
        instr_text.setText("You Lost!")

    win.getMouse()
    win.close()
