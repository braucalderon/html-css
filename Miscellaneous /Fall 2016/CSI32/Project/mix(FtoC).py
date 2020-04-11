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

class FtoCHandler(EventHandler):
  def __init__(self, paper):
    EventHandler.__init__(self)
    self.paper = paper

  def handle(self, event):
    if event.getDescription() == "mouse click":
      paper1 = Canvas(500,400,"linen", "Conversion from Farenheit to Celsius")
      welcome = Text("This program converts from Fahrenheit to Celsius \n \t\t Type in the box", 18, Point(250,50))
      message = TextBox(100,30, Point(250,150))
      paper1.add(message)
      paper1.add(welcome)
      readyButton = Rectangle(100, 50, Point(200,350))
      readyText = Text("Ready!", 18, Point(200,350))
      readyButton.setFillColor("light blue")
      paper1.add(readyButton)
      paper1.add(readyText)

      exitButton = Rectangle(100, 50, Point(400,350))
      exitText = Text("Exit", 18, Point(400,350))
      exitButton.setFillColor("light blue")
      paper1.add(exitButton)
      paper1.add(exitText)
      e = exitButtonHandler(paper1)
      exitButton.addHandler(e)
      exitText.addHandler(e)

      ready = ReadyButtonHandler(message, paper1)
      readyButton.addHandler(ready)
      readyText.addHandler(ready)
      startEventHandling()
      

    
class ReadyButtonHandler(EventHandler):
  def __init__(self, message, paper1):
    EventHandler.__init__(self)
    self.paper1 = paper1
    self.message = message
    self.result = Text('Waiting for your input' ,12, Point(300, 250))
    self.paper1.add(self.result)

  def handle(self, event):
    if event.getDescription() == "mouse click":
      newMessage = int(self.message.getMessage())
      FtoC = (newMessage - 32) * 5/9
      #conversion = Text("Conversion =", 18, Point(150,250))
      self.result.setMessage(str(FtoC))
      
      #self.paper1.add(Conversion)
     
      
      
      

    
##    readyButton = Rectangle(100, 80, Point(200,350))
##    readyText = Text("Ready!", Point(200,350))
##    readyButton.setFontSize(12)
##    readyButton.setFillColor("light blue")
##    paper1.add(readyButton)
##    paper1.add(readyText)
    







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
  button2.addHandler(FtoCHandler(paper))

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
