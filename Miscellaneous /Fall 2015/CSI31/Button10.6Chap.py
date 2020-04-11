#Program that uses button class
# 10.6

import graphics
from graphics import *


class Button:

    def _init_ (self, win, center, width, heigh, label):
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin = x - w
        self.xmax = x + w
        self.ymin = y - h
        self.ymax = y + h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle (p1, p2)
        self.rect.setFill ('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def Clicked(self, pt):
        return True 



def main():
    win=GraphWin('testwindow', 200, 200)
    win.setCoords(0, 0, 100, 100)
    count_button = Button(win,Point (50,20), 40, 20, "Click Me")
    reset_button = Button(win,Point(20, 80), 30, 20, "Reset")
    quit_button = Button(win,Point (80,80),30,20, "Quit")
    value = ord("0")
    number = Text(Point(50,50),chr(value))
    number.draw(win)
    pt=win.getMouse()
    while not quit_button.Clicked(pt):
        if count_button.Cmalicked(pt):
            value = value + 1
            number.setText(chr(value))
        if reset_button.clicked(pt):
            value = ord("0")
            number.setText(chr(value))
        pt=win.getMouse()         
