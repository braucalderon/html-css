from cs1graphics import *
import time


class ShapeHandler(EventHandler):
    def __init__(self):
        EventHandler.__init__(self)
        self._mouseDragged = False

    def handle(self,event):
        shape = event.getTrigger()
        if event.getDescription() == 'mouse drag':
            old = event.getOldMouseLocation()
            new = event.getMouseLocation()
            shape.move(new.getX()-old.getX(), new.getY()-old.getY())
            self._mouseDragged = True
        elif event.getDescription()== 'mouse click':
            self._mouseDragged = False
        elif event.getDescription() == 'mouse release':
            if not self._mouseDragged:
                shape.scale(1.5)
        elif event.getDescrition()== 'mouse click':
            shape.setFillColor('blue')
        
       
            
class NewShapeHandler(EventHandler):
    def __init__(self):
        EventHandler.__init__(self)
        self._shapeCode = 0
        self._handler = ShapeHandler()

    def handle(self,event):
        if event.getDescription() == 'mouse click':
            if self._shapeCode == 0:
                s = Polygon(Point(50,50), Point(0,-5))
            elif self._shapeCode == 1:
                s = Polygon(Point(event.getMouseLocation().getX(), event.getMouseLocation().getY()), Point(event.getMouseLocation().getX(), event.getMouseLocation().getY()))
                
            self._shapeCode = (self._shapeCode + 1) % 2
            s.move(event.getMouseLocation().getX(), event.getMouseLocation().getY())
            s.setFillColor('blue')
            event.getTrigger().add(s)
            s.addHandler(self._handler)


def main():
    
    paper=Canvas(500, 500, 'white', 'Fibonacci Graphic')
    paper.addHandler(NewShapeHandler())
    startEventHandling()



main()








    
