import graphics
from graphics import *

class Button:
    
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
        self.rect.setFill('white')
        self.rect.setOutline('red')
        self.label = Text(center, label)
        self.label.setFill('black')
##        self.linex=linex()
##        self.line=linex(Text(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax)) )
        
        self.rect.draw(win)
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
        self.label.setFill('black')
        self.rect.setWidth(1)
        self.active = False


        
#How can I define (line) into the class button or making another class?
        
##class Line(Button):
##
##    def __init__(self, win, center, width, height, label, linex):
##        Button.__init_(self, win, center, width, height, label)
    
        

        
def letter():
    player=""
    player1=""
    
    while not player
     
    

def main():
    
     
     win = GraphWin("Tic Tac Toe", 400, 400)
     win.setCoords(0, 0, 100, 100)
     
     door1=Button(win,Point(50,50), 50, 30, "Click here to start the game")
     door1.activate()
     pt=win.getMouse()
      
        
     door2=Button(win,Point(30, 70), 20, 20,"")
     door2.activate()
     door3=Button(win,Point(50, 70), 20, 20,"")
     door3.activate()
     door4=Button(win,Point(70, 70), 20, 20,"")
     door4.activate()
     door5=Button(win,Point(30, 50), 20, 20,"")
     door5.activate()
     door6=Button(win,Point(50, 50), 20, 20,"")
     door6.activate()
     door7=Button(win,Point(70, 50), 20, 20,"")
     door7.activate()
     door8=Button(win,Point(30, 30), 20, 20,"")
     door8.activate()
     door9=Button(win,Point(50,30), 20, 20,"")
     door9.activate()
     door10=Button(win,Point(70, 30), 20, 20,"")
     door10.activate()
     door11=Button(win,Point(90,5), 20, 8, "Quit the Game")
     door11.activate()
     
         
    
     
     
     
     pt=win.getMouse()
     while not door11.clicked(pt):
           color = "blue" 
           while color == "blue":
               

               if door2.clicked(pt) and door2.active:
                   door2.deactivate()
                   door2.linex()
               
               if door3.clicked(pt) and door3.active:
                   door3.deactivate()
                   color

              
               if door4.clicked(pt) and door4.active:
                   door4.deactivate()
                   color

                
               if door5.clicked(pt) and door5.active:
                  door5.deactivate()
                  color

               if door6.clicked(pt) and door6.active:
                  door6.deactivate()
                  color

               if door7.clicked(pt) and door7.active:
                   door7.deactivate()
                   color

               if door8.clicked(pt) and door8.active:
                   door8.deactivate()
                   color
            
               if door9.clicked(pt) and door9.active:
                   door9.deactivate()
                   color
            
               if door10.clicked(pt) and door10.active:
                   door10.deactivate()
                   color

     
               
     win.close()                    




main()

     
     
     



