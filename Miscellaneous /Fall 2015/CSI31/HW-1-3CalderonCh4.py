import graphics
from graphics import *
import time

win=GraphWin('Face', 250, 250)

center=Point(120, 120)
circ=Circle(center, 90)
circ.setFill('yellow')
circ.setOutline('black')
circ.draw(win)
time.sleep(1)
leftEye=Circle(Point(80, 90), 7)
leftEye.setFill('black')
leftEye.setOutline('black')
rightEye=leftEye.clone()
rightEye.move(75,0)
rightEye.draw(win)
leftEye.draw(win)
time.sleep(1)
line=Line(Point(70, 170), Point(170, 160))
line.setFill('black')
line.setOutline('black')
line.draw(win)
oval=Oval(Point(180,30), Point(20, 80))
oval.setFill('black')
oval.setOutline('red')
oval.draw(win)

