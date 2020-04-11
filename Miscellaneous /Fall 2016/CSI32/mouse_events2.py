# Description of the program:
# Program creates a graphics window 700 pixels by 600 pixels
# Then on any mouse event (click, release or drag) it informs the user
# about it in the graphics window

from cs1graphics import *
from time import sleep
from sys import exit

class M_EventHandler(EventHandler):
    ''' this handler class identifies a type of mouse event and notifies the user

        there are three types of mouse events:
        Mouse Click
        Mouse Release
        Mouse Drag'''

    
    def __init__(self,textObj):
        ''' constructor calls/invokes the constructor of the EventHandler class,
            and changes the message that displayes type of the mouse event'''
        
        EventHandler.__init__(self)
        self._text=textObj
        self._text.setMessage('No mouse events yet')

    def handle(self,event):
        ''' handler notifies the user of the type of the mouse event,
            otherwise (if it is not a mouse event) does nothing'''
        p=event.getMouseLocation() # get location of Mouse - point
        
        if event.getDescription() == 'mouse click':
            self._text.setMessage('mouse click at ' + str(p))
            #print('mouse click')
        elif event.getDescription() == 'mouse release':
            self._text.setMessage('mouse release at ' + str(p))
            #print('mouse release')

        elif event.getDescription() == 'mouse drag':
            self._text.setMessage('mouse drag at ' + str(p))
            #print('mouse drag')
        else:
            self._text.setMessage('not a mouse event at '+ str(p))
            #print('not a mouse event')

class ExitButtonHandler(EventHandler):
    ''' handler class for program exit '''

    def __init__(self,paper,textObj):
        ''' constructor calls/invokes the constructor of the EventHandler class,
            and stores the reference to the Canvas instance (paper) and to the
            message as attributes'''
        
        EventHandler.__init__(self)
        self._paper = paper
        self._text = textObj
        #print("constructed an ExitButtonHandler")

    def handle(self,event):
        ''' if user clicks of the Exit Button,
        Canvas is closed and program is terminated '''

        #print("Exit Button is clicked")

        if event.getDescription() in ('mouse click','mouse release','mouse drag'):
            self._text.setMessage('Terminating the program...')
            self._paper.close()
            exit()    

def main():
    paper=Canvas(700,600,'light yellow','Playing with mouse events')

    # First part of the message - stays unchanged 
    text1=Text('Event:',18,Point(50,550))
    text1.setFontColor('dark blue')
    paper.add(text1)

    # Second part of the message - changes according to the type of
    # a mouse event
    text2=Text('',18,Point(300,550))
    paper.add(text2)

    # create the handler  for identification of mouse event
    mouseEvent = M_EventHandler(text2) 
    #print('Activating event handler')

    # Exit Button
    ExitButton = Button("Exit",Point(600,555))
    ExitButton.setFillColor('light green')
    ExitButton.setFontSize(18)
    paper.add(ExitButton)

    # create the handler for program termination 
    exitEvent = ExitButtonHandler(paper,text2)

    # activate the handler for identification of mouse event
    paper.addHandler(mouseEvent) 
    #print('Event handler should be working now')

    # activate the handler for Exit Button
    ExitButton.addHandler(exitEvent) 
    #print('Second event handler should be working now')
    
    
main()    
