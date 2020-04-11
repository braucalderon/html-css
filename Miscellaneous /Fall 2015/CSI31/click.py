from graphics import *

def main():
    win=GraphWin('Click Me!',350,350)
    for i in range(15):
        p=win.getMouse()
        print("You clicked at:", p.getX(), p.getY())

main()
