from cs1graphics import *
from time import sleep

class Clicks(EventHandler):

    def __init__(self,t):
        self.t = t

    def handle(self,event):
        if event.getDescription() == 'mouse click':
            p = event.getMouseLocation()
            print(p) # printing the coordinates of the point
            self.t.setMessage('You clicked at point '+str(p)+'.\n Continue clicking anywhere in the window.')
            
            ball=Circle(8,p)
            ball.setFillColor('red')
            win = event.getTrigger()
            win.add(ball)

class exitButton(EventHandler):

    def __init__(self,win,t):
        self.w = win
        self.t = t

    def handle(self,event):
        self.t.setMessage('Good Buy!') # changing message to display "Good Buy!"
        self.w.close()
        

def main():

    paper=Canvas(700,600,'light yellow','Playing with clicks')

    t=Text('click anywhere in the window',18)
    t.move(240,550)
    
    paper.add(t)
    
    # exit button
    button = Button("EXIT",Point(600,555))
    button.setFillColor("light green")
    button.setBorderColor("green")
    button.setFontSize(18)
    paper.add(button)

    e = exitButton(paper,t)
    button.addHandler(e)

    c = Clicks(t)
    paper.addHandler(c)
    #startEventHandling()


main()    

