from cs1graphics import *

class BasicHandler(EventHandler):
    def handle(self,event):
        print("Event Triggered")

def main():

    simple = BasicHandler()
    paper = Canvas(700,600,"light yellow","no Title")
    paper.addHandler(simple) # registering handler simple
    startEventHandling()

main()    
