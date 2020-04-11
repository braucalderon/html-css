from cs1graphics import *

class TallyHandler(EventHandler):
    def __init__(self,textObj):
        EventHandler.__init__(self)
        self._count=0
        self._text=textObj
        self._text.setMessage(str(self._count))

    def handle(self,event):
        if event.getDescription() == 'mouse click':
            self._count += 1
            self._text.setMessage(str(self._count))
            print('Event Tiggered. Count:',self._count)

def main():

    paper=Canvas(700,600,'light yellow')
    score=Text('',20,Point(300,300))
    paper.add(score)

    referee=TallyHandler(score)
    paper.addHandler(referee) # registering handler
    startEventHandling()

main()    
