# Braulio Calderon
# Final Project
# Matrix Arithmetric


from cs1graphics import *
from sys import exit
import time


class ExitButtonHandler(EventHandler):
  def __init__(self,paper):
    EventHandler.__init__(self)
    self._paper = paper

  def handle(self,event):
    if event.getDescription() == "mouse click":
      self._paper.close()
      exit(0)


class addHandler(EventHandler):
  def __init__(self, paper, A, B):
    EventHandler.__init__(self)
    self._paper = paper
    self._A = A
    self._B = B
    

  def handle(self, event):
    if event.getDescription() == "mouse click":
      paper1 = Canvas(200,200,'white', 'Addition')
      r2 = matrix(self._A,self._B)
      result2= display(r2)

      
      title1=Text('Matrix | 1 & 2 |', 10, Point(50,25))
      title1.setFontColor('black')
      title = Text(result2, 13, Point (100, 90))
      title.setFontColor('blue')
      paper1.add(title)
      paper1.add(title1)

      line=Rectangle(190,50, Point(100,170))
      line.setFillColor('gray')
      line.setBorderColor('gray')
      paper1.add(line)

      text=Text('Result Uploaded', 10, Point (100, 130))
      text.setFontColor('black')
      paper1.add(text)
      
      line1=Button('Addition', Point(100, 170))
      line1.setFontSize(12)
      line1.setFontColor('gray')
      line1.setBorderColor('gray')
      paper1.add(line1)

      startEventHandling()
      
      
class mulHandler(EventHandler):
  def __init__(self, paper, A, B):
    EventHandler.__init__(self)
    self._paper = paper
    self._A = A
    self._B = B
    
  def handle(self, event):
    
    if event.getDescription() == "mouse click":
      paper2 = Canvas(200,200,'white', 'Multiplication')
      r = matrix_mult(self._A,self._B)
      result= display(r)

      
      title1=Text('Matrix | 1 & 2 |', 10, Point(50,25))
      title1.setFontColor('black')
      title = Text(result, 13, Point (100, 90))
      title.setFontColor('blue')
      paper2.add(title1)
      paper2.add(title)

      line=Rectangle(190,50, Point(100,170))
      line.setFillColor('gray')
      line.setBorderColor('gray')
      paper2.add(line)

      text=Text('Result Uploaded', 10, Point (100, 130))
      text.setFontColor('black')
      paper2.add(text)
      
      line1=Button('Multiplication', Point(100, 170))
      line1.setFontSize(12)
      line1.setFontColor('gray')
      line1.setBorderColor('gray')
      paper2.add(line1)

      startEventHandling()

class trasHandler(EventHandler):
  def __init__(self, paper, A, B):
    EventHandler.__init__(self)
    self._paper = paper
    self._A = A
    self._B = B

  def handle(self, event):
    
    if event.getDescription() == "mouse click":
      paper3 = Canvas(300,200,'white', 'Transpose')
      r = transpose(self._A)
      result= display(r)
      
      r1 = transpose(self._B)
      result1 = display(r1)


      message=Text('Matrix', 10, Point(140, 25))
      message.setFontColor('black')
      paper3.add(message)
      
      title1=Text('| 1 |', 10, Point(90,25))
      title1.setFontColor('black')
      title = Text(result, 13, Point (70, 90))
      title.setFontColor('blue')
      paper3.add(title)
      paper3.add(title1)

      title2=Text('| 2 |', 10, Point(190,25))
      title2.setFontColor('black')
      titlee = Text(result1, 13, Point (220, 90))
      titlee.setFontColor('blue')
      paper3.add(titlee)
      paper3.add(title2)

      line=Rectangle(290,50, Point(150,170))
      line.setFillColor('gray')
      line.setBorderColor('gray')
      paper3.add(line)

      text=Text('Result of both Matrices',10, Point(150,130))
      text.setFontColor('black')
      paper3.add(text)
      
      line1=Button('Transpose',Point(150, 170))
      line1.setFontSize(13)
      line1.setFontColor('gray')
      line1.setBorderColor('gray')
      paper3.add(line1)

      
      
      startEventHandling()

      

def transpose(A):

    return [[A[j][i] for j in range(0, len(A[i]))] for i in range(0, len(A))]
  

def matrix_mult(A,B):

  
  
  r=[]
  for k in range(len(A)):
    tmp=[]
    for i in range(len(B[0])):
      for j in range(len(A[0])):
        tmp.append(A[k][i] * B[k][i])
    r.append(tmp)
          

  return r

           
def matrix(A,B):

    
  r=[]
  for k in range(len(A)):
      tmp=[]
      for i in range(len(A[0])):
          tmp.append(A[k][i]+B[k][i])
      r.append(tmp)    

  return r

def processdata(f_data): 
  rows = len(f_data)
  
  A=list()

  cols=0
  for r in range(rows):
      line=f_data[r].split()

      if r == 0: 
          cols=len(line)
          print('Number of Columns in the file',cols)

      if len(line) != cols:
          print('Warning: line %d:'%(cols+1))

          raise ValueError('Colums are not equal')

      line_int=[int(elem) for elem in line]
          
      A.append(line_int)

  return A


def display(C): 
    
  m='' 
  cols=len(C[0]) 
  
  for i in range(len(C)): 
      for j in range(cols):
          m+=(str(C[i][j]))
          m+=(" ")
              
      m+="\n"
  print()
  return m 

def main():

  while True:
      #fname=input('\nPlease input the first file: ')
      #fname1=input('Please input the second file: ')

      try:
          f=open('matrix1.txt')
          f1=open('matrix2.txt')
          break
      
      except ValueError:
          print ('\nOne of the files cannot be opened')

      except FileNotFoundError:
          print ('\nOne of the files could not be found' )
      
  f_data= f.readlines()
  f1_data= f1.readlines()
  
  A=processdata(f_data)
  B=processdata(f1_data)

  D1=display(A)
  D2=display(B)
  
  
  

  paper=Canvas(400,250, 'white', 'Matrix Arithmetic')
  
  
#______________________

  #Rectangle
  line=Rectangle(400,70,Point(199,220))
  line.setFillColor('gray')
  line.setBorderColor('gray')
  paper.add(line)
#______________________

  #display uplaoded matrices into graphics
  text1=Button('Uploaded Matrices',Point(200,220))
  text1.setFontSize(15)
  text1.setFontColor('blue')
  text1.setBorderColor('gray')
  paper.add(text1)

#______________________
  
  title1=Text('Matrix | 1 |', 10, Point(40,120))
  title1.setFontColor('gray')
  title = Text(D1, 15, Point (100, 150))
  title.setFontColor('blue')
  paper.add(title)
  paper.add(title1)

#______________________

  title2=Text('Matrix | 2 |', 10, Point(240, 120))
  title2.setFontColor('gray')
  title3 = Text(D2, 15, Point(300, 150))
  title3.setFontColor('blue')
  paper.add(title2)
  paper.add(title3)

#_____________________

  button1 = Button('Addition', Point(60, 30))
  button1.setFontSize(12)
  button1.setBorderColor('blue')
  button1.setFontColor('gray')
  paper.add(button1)
  button1.addHandler(addHandler(paper,A,B))
#______________________

  button2 = Button('Multiplication', Point(180, 30))
  button2.setFontSize(12)
  button2.setBorderColor('blue')
  button2.setFontColor('gray')
  paper.add(button2)
  button2.addHandler(mulHandler(paper, A, B))
  
#______________________

  button3 = Button('Transpose', Point(310, 30))
  button3.setFontSize(12)
  button3.setBorderColor('blue')
  button3.setFontColor('gray')
  paper.add(button3)
  button3.addHandler(trasHandler(paper, A, B))

#______________________

  message1 =Text('Press Buttons Above for result', 10,Point(190, 85))
  message1.setFontColor('black')
  paper.add(message1)
  

  message = Text('| Addition | - | Multiplication | - | Transpose |', 10, Point(190,65))
  message.setFontColor('black')
  paper.add(message)

#______________________

  buttone=Button('Exit', Point(380,235))
  buttone.setFontSize(11)
  buttone.setFontColor('gray')
  buttone.setBorderColor('gray')
  paper.add(buttone)

  h=ExitButtonHandler(paper)
  buttone.addHandler(h)



  startEventHandling()

main()
