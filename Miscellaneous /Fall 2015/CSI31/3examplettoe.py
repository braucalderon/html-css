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
    
 #    p1 = None #for now
#     p2 = None #for now
     win = GraphWin("Tic Tac Toe", 400, 400)
     win.setCoords(0, 0, 100, 100)
     win.setBackground('gray')
     
     door1=Button(win,Point(50,50),40, 20, "Welcome to Tic Tac Toe \nClick here to start")
     door1.activate()
     door12=Button(win,Point(10,95), 15, 5, "Player 1 X")
     door12.activate()
     
     door13=Button(win,Point(10,85), 15, 5, "Player 1 O")
     door13.activate()
     
     door14=Button(win,Point(90,95), 15, 5, "Player 2 X")
     door14.activate()
     
     door15=Button(win,Point(90,85), 15, 5, "Player 2 O")
     door15.activate()
     
 
     
      
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
     
 
     
     board = [door2,door3,door4,door5,door6,door7,door8,door9,door10]


     pt=win.getMouse()
     while not door11.clicked(pt):
         
     
         if door12.clicked(pt) or door15.clicked(pt):
            p1 = 'X'
            p2 = 'O'
            door13.deactivate(), door14.deactivate()
            
         if door13.clicked(pt) or door14.clicked(pt):
            p1 = 'O'
            p2 = 'X'
            door12.undraw(), win.door15.undraw()
    
         game = True
         box =[
        #Y    0   1   2  X
             ['','',''], #0
             
             ['','',''], #1
             
             ['','',''], #2
             ]
         #[X][Y]
         #[0][0]
         #[0][1]
         turn = 1
         while(game):
            # print(box)
            # print(turn)
             pt=win.getMouse()
             if(door2.clicked(pt)):
                 door2.deactivate()
                 if(turn == 1): #turn=1 is assigned to p1
                     box[0][0] = p1
                     t = Text(Point((door2.xmin + door2.xmax)/2,(door2.ymin + door2.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2 # is assigned to p2 automatically 
                 else:
                     box[0][0] = p2
                     t = Text(Point((door2.xmin + door2.xmax)/2,(door2.ymin + door2.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
    
             if(door3.clicked(pt)):
                 door3.deactivate()
                 if(turn == 1):
                     box[0][1] = p1
                     t = Text(Point((door3.xmin + door3.xmax)/2,(door3.ymin + door3.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[0][1] = p2
                     t = Text(Point((door3.xmin + door3.xmax)/2,(door3.ymin + door3.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door4.clicked(pt)):
                 door4.deactivate()
                 if(turn == 1):
                     box[0][2] = p1
                     t = Text(Point((door4.xmin + door4.xmax)/2,(door4.ymin + door4.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[0][2] = p2
                     t = Text(Point((door4.xmin + door4.xmax)/2,(door4.ymin + door4.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door5.clicked(pt)):
                 door5.deactivate()
                 if(turn == 1):
                     box[1][0] = p1
                     t = Text(Point((door5.xmin + door5.xmax)/2,(door5.ymin + door5.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[1][0] = p2
                     t = Text(Point((door5.xmin + door5.xmax)/2,(door5.ymin + door5.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door6.clicked(pt)):
                 door6.deactivate()
                 if(turn == 1):
                     box[1][1] = p1
                     t = Text(Point((door6.xmin + door6.xmax)/2,(door6.ymin + door6.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[1][1] = p2
                     t = Text(Point((door6.xmin + door6.xmax)/2,(door6.ymin + door6.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door7.clicked(pt)):
                 door7.deactivate()
                 if(turn == 1):
                     box[1][2] = p1
                     t = Text(Point((door7.xmin + door7.xmax)/2,(door7.ymin + door7.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[1][2] = p2
                     t = Text(Point((door7.xmin + door7.xmax)/2,(door7.ymin + door7.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door8.clicked(pt)):
                 door8.deactivate()
                 if(turn == 1):
                     box[2][0] = p1
                     t = Text(Point((door8.xmin + door8.xmax)/2,(door8.ymin + door8.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[2][0] = p2
                     t = Text(Point((door8.xmin + door8.xmax)/2,(door8.ymin + door8.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door9.clicked(pt)):
                 door9.deactivate()
                 if(turn == 1):
                     box[2][1] = p1
                     t = Text(Point((door9.xmin + door9.xmax)/2,(door9.ymin + door9.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[2][1] = p2
                     t = Text(Point((door9.xmin + door9.xmax)/2,(door9.ymin + door9.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
             if(door10.clicked(pt)):
                 door10.deactivate()
                 if(turn == 1):
                     box[2][2] = p1
                     t = Text(Point((door10.xmin + door10.xmax)/2,(door10.ymin + door10.ymax)/2),p1)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 2
                 else:
                     box[2][2] = p2
                     t = Text(Point((door10.xmin + door10.xmax)/2,(door10.ymin + door10.ymax)/2),p2)
                     t.setFill('blue')
                     t.setOutline('blue')
                     t.draw(win)
                     turn = 1
    
            #check for winning
             if(turn == 1):
                 if(box[0][0] == p1 and box[0][1] == p1 and box[0][2] == p1     #1 horizontal / top to bottom
                    or box[1][0] == p1 and box[1][1] == p1 and box[1][2] == p1  #2 horizontal
                    or box[2][0] == p1 and box[2][1] == p1 and box[2][2] == p1  #3 horizontal
                    or box[0][0] == p1 and box[1][0] == p1 and box[2][0] == p1  #1 right to left vertical  
                    or box[0][1] == p1 and box[1][1] == p1 and box[2][1] == p1  #2 vertical
                    or box[0][2] == p1 and box[1][2] == p1 and box[2][2] == p1  #3 vertical
                    or box[0][0] == p1 and box[1][1] == p1 and box[2][2] == p1  #1 cross 
                    or box[0][2] == p1 and box[1][1] == p1 and box[2][0] == p1):#2 cross 
                     print('P1 wins')
                     game = False
                     turn = 2
             else:
                 if(box[0][0] == p2 and box[0][1] == p2 and box[0][2] == p2    #1
                    or box[1][0] == p2 and box[1][1] == p2 and box[1][2] == p2 #2
                    or box[2][0] == p2 and box[2][1] == p2 and box[2][2] == p2 #3
                    or box[0][0] == p2 and box[1][0] == p2 and box[2][0] == p2 #1
                    or box[0][1] == p2 and box[1][1] == p2 and box[2][1] == p2 #2
                    or box[0][2] == p2 and box[1][1] == p2 and box[2][2] == p2 #3
                    or box[0][0] == p2 and box[1][1] == p2 and box[2][2] == p2 #1
                    or box[0][2] == p2 and box[1][1] == p2 and box[2][0] == p2): #2
                     print('P2 wins')
                     game = False
     win.close()                
     

main()              
                       






     
     
     


