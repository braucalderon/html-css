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
 #       self.rect.line( Point(self.xmin, self.ymin), Point(self.xmax, self.ymax) )
        
        self.rect.draw(win)
        self.label.draw(win)

        
        self.deactivate()
        
##    def circle(self, win, pt):
##        x = pt.getX()
##        y = pt.getY()
##        self.cir=Circle(Point(x,y),5)
##        self.cir.setFill('black')
##        self.cir.draw(win)
        
##    def linex(self, win, pt):
##        x = pt.getX()
##        y = pt.getY()
##        self.rect=Rectangle(Point(x,y), Point(x,y))
##        self.rect.setFill('black')
##        self.rect.draw(win)

    
        
    
    
            
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

    
        
def main():
    
     p1 = None #for now
     p2 = None #for now
     win = GraphWin("Tic Tac Toe", 400, 400)
     win.setCoords(0, 0, 100, 100)
     win.setBackground('gray')
     
     door1=Button(win,Point(50,50),40, 20, "Welcome to Tic Tac Toe \nClick here to start")
     door1.activate() 
     pt=win.getMouse()
     door1.clicked(pt)
     
      
     win.setBackground('lightgray')   
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
     
     door11=Button(win,Point(85,5), 23, 8, "Quit the Game")
     door11.activate()
     
     door12=Button(win,Point(10,95), 15, 5, "Player 1 X")
     door12.activate()
     
     door13=Button(win,Point(10,85), 15, 5, "Player 1 O")
     door13.activate()
     
     door14=Button(win,Point(90,95), 15, 5, "Player 2 X")
     door14.activate()
     
     door15=Button(win,Point(90,85), 15, 5, "Player 2 O")
     door15.activate()

     reset=Button(win,Point(15,20), 15, 5, "Reset")
     reset.activate()
                  
     board = [door2,door3,door4,door5,door6,door7,door8,door9,door10]




     pt=win.getMouse()
     if door12.clicked(pt) or door15.clicked(pt):
        p1 = 'X'
        p2 = 'O'
        door13.deactivate(), door14.deactivate()
     if door13.clicked(pt) or door14.clicked(pt):
        p1 = 'O'
        p2 = 'X'
        door12.deactivate(), door15.deactivate()

     game = True
     box =[
    #Y    0   1   2  X
         ['','',''], #0
         
         ['','',''], #1
         
         ['','',''], #2
         ]
     #[X][Y]
     turn = 1
     while(game):
         print(box)
         print(turn)
         pt=win.getMouse()
         if(door2.clicked(pt)):
             door2.deactivate()
             if(turn == 1):
                 box[0][0] = p1
                 t = Text(Point((door2.xmin + door2.xmax)/2,(door2.ymin + door2.ymax)/2),p1)
                 t.draw(win)
                 turn = 2
             else:
                 box[0][0] = p2
                 t = Text(Point(door2.xmin,door2.ymin),p2)
                 t.draw(win)
                 turn = 1

         if(door3.clicked(pt)):
             if(turn == 1):
                 box[0][1] = p1
                 turn = 2
             else:
                 box[0][1] = p2
                 turn = 1
         if(door4.clicked(pt)):
             if(turn == 1):
                 box[0][2] = p1
                 turn = 2
             else:
                 box[0][2] = p2
                 turn = 1
         if(door5.clicked(pt)):
             if(turn == 1):
                 box[1][0] = p1
                 turn = 2
             else:
                 box[1][0] = p2
                 turn = 1
         if(door6.clicked(pt)):
             if(turn == 1):
                 box[1][1] = p1
                 turn = 2
             else:
                 box[1][1] = p2
                 turn = 1
         if(door7.clicked(pt)):
             if(turn == 1):
                 box[1][2] = p1
                 turn = 2
             else:
                 box[1][2] = p2
                 turn = 1
         if(door8.clicked(pt)):
             if(turn == 1):
                 box[2][0] = p1
                 turn = 2
             else:
                 box[2][0] = p2
                 turn = 1
         if(door9.clicked(pt)):
             if(turn == 1):
                 box[2][1] = p1
                 turn = 2
             else:
                 box[2][1] = p2
                 turn = 1
         if(door10.clicked(pt)):
             if(turn == 1):
                 box[2][2] = p1
                 turn = 2
             else:
                 box[2][2] = p2
                 turn = 1
         if (reset.clicked(pt)):
             reset.activate()
             game = True
             box =[['','',''],
                   ['','',''], 
                   ['','','']]
              
 

        #check for winning
         if turn == 1:
             if(box[0][0] == p1 and box[0][1] == p1 and box[0][2] == p1):
                 print('P1 wins')
             if( box[1][0] == p1 and box[1][1] == p1 and box[1][2] == p1
                or box[2][0] == p1 and box[2][1] == p1 and box[2][2] == p1
                or box[0][0] == p1 and box[1][0] == p1 and box[2][0] == p1
                or box[0][1] == p1 and box[1][1] == p1 and box[2][1] == p1
                or box[0][2] == p1 and box[2][1] == p1 and box[2][2] == p1
                or box[0][0] == p1 and box[1][1] == p1 and box[2][2] == p1
                or box[2][0] == p1 and box[1][1] == p1 and box[0][2] == p1):
                  print('P1 wins')
                  game = False
         else:
             if(box[0][0] == p2 and box[0][1] == p2 and box[0][2] == p2
                or box[1][0] == p2 and box[1][1] == p2 and box[1][2] == p2
                or box[2][0] == p2 and box[2][1] == p2 and box[2][2] == p2
                or box[0][0] == p2 and box[1][0] == p2 and box[2][0] == p2
                or box[1][0] == p2 and box[1][1] == p2 and box[2][1] == p2
                or box[2][0] == p2 and box[2][1] == p2 and box[2][2] == p2
                or box[0][0] == p2 and box[1][1] == p2 and box[2][2] == p2
                or box[2][0] == p2 and box[1][1] == p2 and box[0][2] == p2):
                  print('P1 wins')
                  game = False

main()              
                       






     
     
     


