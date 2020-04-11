from cs1graphics import *

class TallyHandler(EventHandler):
    def __init__(self,textObj):
        EventHandler.__init__(self)
        self._count=0
        self._text=textObj
        self._text.setMessage(str(self._count))

    def handle(self,event):
        self._count += 1
        self._text.setMessage(str(self._count))
        print('Event Tiggered. Count:',self._count)
        
class ExitButton(EventHandler):

    def __init__(self,win):
        self.win = win

    def handle(self,event):
        self.win.close()
        

def main():

    paper=Canvas(700,600,'light yellow')
    score=Text('',20,Point(300,300))
    paper.add(score)

    # exit button
    button=Button("EXIT",Point(600,555))
    button.setFillColor("light green")
    button.setBorderColor("green")
    button.setFontSize(18)

    paper.add(button)


    referee=TallyHandler(score)
    paper.addHandler(referee) # registering counting handler
    e = ExitButton(paper)
    button.addHandler(e) # registering exit button handler 

main()    
