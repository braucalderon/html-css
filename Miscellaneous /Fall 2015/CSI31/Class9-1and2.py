

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
    
    value = ord("a")
    number = Text(Point(50,50),chr(value))
    number.draw(win)
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if count_button.clicked(pt):
            value = value + 1
            number.setText(chr(value))

        if value == ord("z"):
            count_button.deactivate()

        if reset_button.clicked(pt):
             value = ord("a")
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
    Quit = Button(win,Point(95,5),10,10,"Quit")
    

    door1.activate()
    door2.activate()
    door3.activate()
    Quit.activate()
    
    Wins = 0
    Lost = 0
    
    instr_text = Text(Point(50,20),"Click a door")
    instr_text.draw(win)
    WinsCount_text = Text(Point(10,5),"Wins:")
    WinsCount_text.draw(win)
    LostCount_text = Text(Point(25,5),"Lost:")
    LostCount_text.draw(win)

    Wins_text = Text(Point(17,5),Wins)
    Wins_text.draw(win)
    Lost_text = Text(Point(31,5),Lost)
    Lost_text.draw(win)

    
    Multiplegameover = False
    while Multiplegameover == False:
        # NOTE: I MADE CHANGE IN NEXT LINE
        hasWon,badclickcheck,Multiplegameover = Singlegame(win,door1,door2,door3,Quit,instr_text)
        if hasWon == True:
            Wins+=1
        else:
            if badclickcheck ==False:
                Lost+=1
        Wins_text.setText(Wins)
        Lost_text.setText(Lost)
        
            
def Singlegame(win,door1,door2,door3,Quit, instr_text):   
    Gameover = False
    pt = win.getMouse()
    badclickcheck = False
    quitGame = False

    while Gameover == False:
        hasWon = False
        prize = randrange(1,4)

        if door1.clicked(pt):
            Gameover = True
            if prize == 1:
                hasWon = True

        if door2.clicked(pt):
            Gameover = True
            if prize == 2:
                hasWon = True

        if door3.clicked(pt):
            Gameover = True
            if prize == 3:
                hasWon = True

        if Quit.clicked(pt):
            win.close()
            # NOTE: I MADE CHANGE IN NEXT LINE
            quitGame = True

        if hasWon:
            instr_text.setText("You Won!")

        else:
            if not door1.clicked(pt) and not door2.clicked(pt) and not door3.clicked(pt):
                instr_text.setText("Click a door this time!")
                badclickcheck = True
            else:
                instr_text.setText("You Lost!")

        # NOTE: I MADE CHANGE IN NEXT LINE
        return hasWon,badclickcheck,quitGame

