from cs1graphics import *
from sys import exit

def welcomeMSG(paper):
  pass

class exitButtonHandler(EventHandler):
  """ takes care of the Exit button.
  When the button is clicked, the program is terminated. """
  

  def __init__(self,paper):
    EventHandler.__init__(self)
    self.paper = paper

  def handle(self,event):
    if event.getDescription() == "mouse click":
      self.paper.close()
      exit(0)


class fchandler(EventHandler):
  def __init__(self, paper):
    EventHandler._init__(self)

  def handler(self, event):
    pass


  def handler(self, event):
    pass
  

def main():
  width = 800
  height = 600
  paper = Canvas(width,height,"white","Mix of different things")

  # display welcome message with instructions
  welcomeMSG(paper)

  # C to F button
  button1 = Button("C to F",Point(width//4,height//3))
  button1.setFontSize(18)
  button1.setFillColor("light blue")
  paper.add(button1)

  # F to C button
  button2 = Button("F to C",Point(width//2,height//3))
  button2.setFontSize(18)
  button2.setFillColor("light blue")
  paper.add(button2)

  # distance button
  button3 = Button("distance",Point(3*width//4,height//3))
  button3.setFontSize(18)
  button3.setFillColor("light blue")
  paper.add(button3)

  # pounds to kilograms
  button4 = Button("LB to KG",Point(width//4,height//2))
  button4.setFontSize(18)
  button4.setFillColor("light blue")
  paper.add(button4)

  # kilograms to pounds
  button5 = Button("KG to LB",Point(width//2,height//2))
  button5.setFontSize(18)
  button5.setFillColor("light blue")
  paper.add(button5)

  # exit button
  buttonE = Button("EXIT",Point(width-100,height-50))
  buttonE.setFontSize(18)
  buttonE.setFillColor("light green")
  paper.add(buttonE)
  buttonE.addHandler(exitButtonHandler(paper))
  startEventHandling()

main()
