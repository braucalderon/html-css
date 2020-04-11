# This is the Future Value Problem

import graphics
from graphics import *


#Create the initial window
def createLabelWindow():
    window=GraphWin("Investmen", 320, 240)
    window.setCoords(-1.75, -200, 11.5, 10400)# X left, X right, Y bottom, Y top 
    window.setBackground("white")
    Text(Point(-1,0), ' 0.OK').draw(window)
    Text(Point(-1,2500),' 2.5K').draw(window)
    Text(Point(-1,5000), '5.Ok').draw(window)
    
         
    return window

def drawbar(year, height):
    print("not done yet")

def main():
    print ("This program will take some input and")
    principal=eval(input("What is the principal: "))
    rate=eval(input("What is interest rate: "))

    #Create the initial window
    my_win = createLabelWindow()

    
    
