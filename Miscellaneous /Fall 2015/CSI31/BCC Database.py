import graphics
from graphics import *
from time import*



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
        self.rect.setFill('gray')
        self.rect.setOutline('black')
        self.label = Text(center, label)
        self.label.setFill('black')
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




class Database:

    def __init__(self, fname):
        self.List = []
        self.fname = fname
        infile = open(fname, "r")
        for line in infile:
            b = line.strip('\n').split(',') # = ['reyes'= 0, ' ben'= 1, ' student', ' male', ' hispanic', ' 26', ' 5']
##            print(b[0])#Last
##            print(b[1])#First
##            print(b[2])#Status
##            print(b[3])#Gender
##            print(b[4])#Race
##            print(b[5])#Age
##            print(b[6])#Years
            self.List.append(b)
          

    def listor(self,l,f,s,g,r,a,y):
        LO = []
        
        for i in self.List:
            if i[0] == l or i[1] == f or i[2] == s or i[3] == g or i[4] == r or i[5] == a or i[6] == y:
                LO.append(i)

        return LO
    
    
    def listand(self,l,f,s):
        L = []

        for i in self.List:
            if i[0] == l and i[1] == f and i[2] == s:
                L.append(i)
                
        return L
    
    
    def Output1(self, out):
        K = []
        
        for i in self.List:
            if i == out:
                K.append(i)
                
            return K

 


        
        

  
        
        
        

        
def main():

    
    
    win=GraphWin('Database', 800, 700)
    win.setCoords(0, 0, 100, 100)
    win.setBackground('lightgray')

    Text(Point (50, 95), 'BCC Database').draw(win)
    

    #Boxes
    Text(Point (10, 85), 'Enter File First as .TXT').draw(win)
    stats  = Entry(Point (27, 85),20)
    stats.setText('')
    stats.draw(win)
    
    Text(Point (15, 80), 'Enter Last Name').draw(win)
    last = Entry(Point (30, 80),20)
    last.setText('')
    last.draw(win)
    
    Text(Point (15, 75), 'Enter First Name').draw(win)
    first = Entry(Point (30, 75), 20)
    first.setText('')
    first.draw(win)
     
    
    Text(Point (15, 70), 'Enter Status').draw(win)
    status = Entry(Point (30, 70), 20)
    status.setText('')
    status.draw(win)

    Text(Point (15, 65), 'Enter Gender').draw(win)
    gender = Entry(Point (30, 65), 20)
    gender.setText('')
    gender.draw(win)

    Text(Point (15, 60), 'Enter Race').draw(win)
    race = Entry(Point (30, 60), 20)
    race.setText('')
    race.draw(win)

    Text(Point (15, 55), 'Enter Age').draw(win)
    age = Entry(Point (30, 55), 20)
    age.setText('')
    age.draw(win)

    Text(Point (15, 50), 'Enter Year').draw(win)
    year = Entry(Point (30, 50), 20)
    year.setText('')
    year.draw(win)

    #Text Messages
    MNF = Text(Point (60, 75), '')
    MNF.draw(win)

    Text(Point (15, 20),'Match Found:').draw(win)

    Text(Point (65, 75), 'The File name \n\nMust be type \n\nby the user First').draw(win)


    #Match
    Match = Text(Point(35,15), '')
    Match.draw(win)
    
    
    

    
    #Buttons 
    search=Button(win,Point(50,50), 10,5,'ListOr')
    search.activate()

    search1=Button(win,Point(70,50), 25,5,'Click here\n to search with three attributes only')
    search1.activate()

    delete=Button(win,Point(10,40), 10, 5, 'Clear')
    delete.activate()

    #Special Button Output
    Output=Button(win,Point(30,29), 10, 5, 'Output')
    Output.activate()

    #Output Button / 
    Text(Point (30,40), 'Enter Attribute\n \nEx: Gender').draw(win)
    out = Entry(Point (30,35), 20)
    out.setText('')
    out.draw(win)

    Quit = Button(win,Point(90,5), 10, 5, 'Quit')
    Quit.activate()

    #Reset Button
    reset=Button(win, Point(10, 30), 10, 5, 'Reset')
    reset.activate()

    #Count
    count = Button(win, Point(90, 50), 10, 5, 'Count')
    count.activate()
    
    

    

    

    
    


    while (True):
        pt=win.getMouse()
        if search.clicked(pt): #clicked the Listor button
            file = stats.getText()
            l = last.getText()
            f = first.getText()
            s = status.getText()
            g = gender.getText()
            r = race.getText()
            a = age.getText()
            y = year.getText()
            db = Database(file)
            k = db.listor(l,f,s,g,r,a,y)
            Match.setText(k)
        
        if search1.clicked(pt):
            search1=Button(win,Point(70,50), 25,5,'List And\n All Attributes Must Be Filled')
            search1.activate()
            race.undraw()
            year.undraw()
            age.undraw()
            gender.undraw()
            out.undraw()
            
            if search1.clicked(pt):
                file = stats.getText()
                l = last.getText()
                f = first.getText()
                s = status.getText()
                db = Database(file)
                h = db.listand(l,f,s)
                Match.setText(h)
                        

        if Output.clicked(pt):
            file = stats.getText()
            db = Database(file)
            t = db.Output1(out)
            Match.setText(t)

        if delete.clicked(pt):
            dic = {last.setText(''), first.setText(''), status.setText(''),
                   gender.setText(''), race.setText(''), age.setText(''),
                   year.setText(''), out.setText('')}
            
            
 
        if reset.clicked(pt):
            win.close()
            main()
            
            
            
            
            
            


        if Quit.clicked(pt):
            
            win.close()
            break
            
            
 
            
        if count.clicked(pt):
            file = stats.getText()
            l = last.getText()
            f = first.getText()
            s = status.getText()
            g = gender.getText()
            r = race.getText()
            a = age.getText()
            y = year.getText()
            db = Database(file)
            k = db.listor(l,f,s,g,r,a,y)
            Match.setText(str(len(k)))
            
 
            
            
            
     


        

main()
