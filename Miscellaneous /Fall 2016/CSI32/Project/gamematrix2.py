from cs1graphics import *
from sys import exit



class ExitButtonHandler(EventHandler):
  def __init__(self,paper):
    EventHandler.__init__(self)
    self._paper = paper

  def handle(self,event):
    if event.getDescription() == "mouse click":
      self._paper.close()
      exit(1)


class AdditionHandler(EventHandler):
  
  def __init__(self, paper):
    EventHandler.__init__(self)
    self._paper = paper
    

  def handle(self, event):
    if event.getDescription() == "mouse click":
      paper1 = Canvas(400,400,'white', 'Uploaded Matrices')
      


  

def matrix_mult(A,B):
  r=[]
  for k in range(len(A)):
    tmp=[]
    for i in range(len(A[0])):
      tmp.append(A[k][i] * B[k][i])
      r.append(tmp)    

  #print(r)
  #print()
  return r

           
def matrix(A,B):
    
  r=[]
  for k in range(len(A)):
      tmp=[]
      for i in range(len(A[0])):
          tmp.append(A[k][i]+B[k][i])
      r.append(tmp)    

  #print(r)
  #print()
  return r

def processdata(f_data): # one argument needed to process both files
    # argument must be the object that must be processed 
  rows = len(f_data)
  
  A=list()

  cols=0
  for r in range(rows):
      line=f_data[r].split()

      if r == 0: # getting the number of elements in each string of the list
          cols=len(line)
          print('Number of Columns in the file',cols)

      if len(line) != cols:
          print('Warning: line %d:'%(cols+1))

          raise ValueError('Colums are not equal')

      line_int=[int(elem) for elem in line]
          
      # appent the list of integers to list A as a next element of list A
      A.append(line_int)

  return A



def traspose(A):

    return [[A[j][i] for j in range(0, len(A[i]))] for i in range(0, len(A))]
  

def matrix_mult(A,B):
  r=[[0 for row in range(len(B[0]))] for col in range(len(A))]
  
  for k in range(len(A)):
    for i in range(len(B[0])):
      for j in range(len(A[0])):
        r[k][i]+=(A[k][i] * B[k][i])
          

  #print(r)
  #print()
  return r


def display(C): #any argument can be added
    
  m='' # empty variable, will store result into it
  cols=len(C[0]) # C same as the argument
  
  for i in range(len(C)):# C must be the same as the argument 
      for j in range(cols):
          m+=(str(C[i][j]))# C must be the same as the argument
          m+=(" ")
              
      m+="\n"
  print()
  return m # without it, result cannot be copy into the new file created

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
  
  
  # def processdata() only needs one argument(f_data) to process both files
  A=processdata(f_data)
  B=processdata(f1_data)

  D1=display(A)
  D2=display(B)

  t=matrix(A,B)
  t1=matrix_mult(A,B)
  t2=traspose(A)
  t3=traspose(B)
  add=display(t3)
  

  paper = Canvas(200,200,'white', 'Multiplication')
  

  
  title1=Text('Matrix  | 1 & 2 |', 10, Point(50,25))
  title1.setFontColor('black')
  title = Text(str(add), 14, Point (100, 100))
  title.setFontColor('blue')
  paper.add(title1)
  paper.add(title)

  line=Rectangle(190,50, Point(100,170))
  line.setFillColor('gray')
  line.setBorderColor('gray')
  paper.add(line)

  line1=Button('Multiplication', Point(100, 170))
  line1.setFontSize(12)
  line1.setFontColor('gray')
  line1.setBorderColor('gray')
  paper.add(line1)
  

  
main()
