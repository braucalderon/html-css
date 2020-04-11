#HW 11

from cs1graphics import *
from sys import exit
import random 

class Square(Rectangle):

    def __init__(self, width=120, height=100, center=Point(310,150)):
        Rectangle.__init__(self, width, height, center)

    def setWidth(self,width):
        self.setWidth()

    def setHeight(self, height):
        self.setHeight()

    def getWidth(self):
        return self.Radius()

    def getHeight(self):
        return self.Height()
    

class Circ(Circle):

    def __init__(self, radius=60, center=Point(125, 150)):
        Circle.__init__(self, radius, center)

    def setRadius(self, radius):
        self.setSize()

    def getRadius(self):
        return self.getRadius()


class TallyHandler(EventHandler):
    def __init__(self,textObj):
        EventHandler.__init__(self)
        self._count=0
        self._text=textObj
        self._text.setMessage(str(self._count))
        

    def handle(self,event):
        self._count += 1
        self._text.setMessage(str(self._count))
        shape=event.getTrigger()
        shape.setFillColor(colors())#the def colors is called on here



class ExitButtonHandler(EventHandler):

    def __init__(self,paper):
        
        EventHandler.__init__(self)
        self._paper = paper

    def handle(self,event):
        
        if event.getDescription() == 'mouse click':
            self._paper.close()
            exit(1)    


def colors():
    for i in range(85):
        r= random.randrange(256)
        b= random.randrange(256)
        g= random.randrange(256)
        color = (r, g, b)

    return color
        
    
    

def main():
    
    paper=Canvas(500, 350, 'lightgray', 'HW 11')
    
    
    s=Circ(60, Point(125, 150))
    s.setFillColor('gray')
    s.setBorderWidth(2)
    paper.add(s)

    score=Square(40,25,Point(125, 277))
    score.setFillColor('white')
    paper.add(score)
    score=Text('', 15, Point(125, 280))
    paper.add(score)
    referee=TallyHandler(score)
    s.addHandler(referee)
    score=Text('Score Count', 12, Point(125,250))
    paper.add(score)
    


    s1=Square(120,100,Point(310,150))
    s1.setFillColor('gray')
    s1.setBorderWidth(2)
    paper.add(s1)


    score1=Square(40,25,Point(310,277))
    score1.setFillColor('white')
    paper.add(score1)
    score1=Text('', 15, Point(310,280))
    paper.add(score1)
    referee1=TallyHandler(score1)
    s1.addHandler(referee1)
    score1=Text('Score Count', 12, Point(310,250))
    paper.add(score1)
    
    
    
    ExitButton = Button('Close',Point(460,325))
    ExitButton.setBorderColor('black')
    ExitButton.setBorderWidth(3)
    ExitButton.setFontSize(10)
    paper.add(ExitButton)
    
    h = ExitButtonHandler(paper)
    ExitButton.addHandler(h)
    
    startEventHandling()
    
main()

