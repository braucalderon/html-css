# Matrix Arithmetric (using file input and graphis)
#Design and implement a program that will allow the user to play
#with matrix operations (addition, multiplication and transpose of matrix)

#input:two files(from files)
#the rest: inthe graphics window
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
      exit(1)


class matrix(Layer, EventHandler):
    def __init__(self):
        
        Layer.__init__(self)
        EventHandler.__init__(self)
        
        
        self._addition = Rectangle(100,30,Point(-140,150))
        self._mult = Rectangle(100,30,Point(-10,150))
        self._transpose = Rectangle(100,30,Point(130,150))
        self._matrices = Rectangle(100, 30, Point(-10,100))
        
        buttons = [self._matrices, self._addition,self._mult,self._transpose]
        for b in buttons:
            b.setBorderColor('gray')

        self._add = Text('Addition', 10,Point(-140,150))
        self._add.setFontColor('blue')
        self._mult1 = Text('Multiplication', 10,Point(-10,150))
        self._mult1.setFontColor('blue')
        self._transpose1 = Text('Transpose', 10, Point(130,150))
        self._transpose1.setFontColor('blue')
        self._matrices1 = Text('Matrices', 10, Point(-10,100))

        buttons.extend([self._matrices1, self._add, self._mult1, self._transpose1])
        for obj in buttons:
            self.add(obj)

        for active in buttons:
            active.addHandler(self)

            
    def handle(self, event):
        
        event.getDescription()== 'mouse click'

        if event.getDescription() in (self._matrices, self._matrices1):
            self.display.setText(self._D1)
                
        





def matrix(A,B):
    
  r=[]
  for k in range(len(A)):
      tmp=[]
      for i in range(len(A[0])):
          tmp.append(A[k][i]+B[k][i])
      r.append(tmp)    

  return r

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
                                

    
if __name__=='__main__':

    while True:
      fname=input('\nPlease input the first file: ')
      fname1=input('Please input the second file: ')

      try:
          f=open(fname)
          f1=open(fname1)
          break
      
      except ValueError:
          print ('\nOne of the files cannot be opened')

      except FileNotFoundError:
          print ('\nOne of the files could not be found' )

    f_data = f.readlines()
    f1_data = f1.readlines()

    A=processdata(f_data)
    B=processdata(f1_data)

    D=display(A)
    D1=display(B)

          
    paper=Canvas(400,400)
    matrix1=matrix(A,B)
    paper.add(matrix1)
    matrix1.move(200,200)

    startEventHandling()

    

main()
