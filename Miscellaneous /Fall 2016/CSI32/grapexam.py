from cs1graphics import *
import time

def main():
    
    #paper = Canvas()
    #paper.setBackgroundColor((218,240,248))
    #paper.setWidth(600)
    #paper.setHeight(700)
    #paper.setTitle("First Experiment")

    # creating a graphics window of width 600 pixels and length
    # 700 pixels; background color (R,G,B) = (218,240,248)
    # title: First Experiment
    paper=Canvas(600,700,(218,240,248),"First Experiment")

    # waiting
    time.sleep(2)

    # changing the background color
    paper.setBackgroundColor((245,226,245))

    # waiting
    time.sleep(2)

    # creating/instantiating a rectangle 200pixels X 100pixels
    # with the center point at (300,350)
    r=Rectangle(200,100,Point(300,350))

    # instantiating a circle with radius 100 pixels,
    # and center point at (300,350)
    c=Circle(100,Point(300,350))
    # filling the rectangle with red color
    r.setFillColor('Red')
    r.setDepth(20) # setting the depth
    # filling the circle with blue color
    c.setFillColor('Blue') 
    c.setDepth(40) # setting the depth, circle is deeper that the rectangle

    paper.add(r)  # adding the rectangle to the drawing
    time.sleep(2) # waiting
    
    paper.add(c) # adding the circle to the drawing
    time.sleep(2) # waiting

    paper.remove(r) # removing rectangle
    paper.remove(c) # removing circle

    # instantiating a text object
    m=Text("Hello! How are you?")
    #message.setFontColor("Green")
    m.move(140,50) # moving 50 pixels down and 140 pixels to the right
    paper.add(m) # adding to the drawing

    time.sleep(6)
    
    paper.close()
    

main()    
