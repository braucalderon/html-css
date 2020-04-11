#Ismael Garrido
#MatrixProgram.py
#Homework13
#Prof.Natalia Novak

from cs1graphics import *
from sys import exit

class exitButtonHandler(EventHandler):
     """ takes care of the Exit button."""
     def __init__(self,paper):
          EventHandler.__init__(self)
          self.paper = paper
     def handle(self,event):
          if event.getDescription() == "mouse click":
               self.paper.close()
               exit(0)


class matrixAddHandler(EventHandler):
     def __init__(self, paper, A, B):
          EventHandler.__init__(self)
          self.paper = paper
          self.A = A
          self.B = B
          
     def handle(self,event):
          if event.getDescription() == "mouse click":
               paper1 = Canvas(400,400,"linen", "Matrix Addition")
               r = matrixAddition(self.A, self.B)
               result = display(r)
               text = Text(result, 26, Point(200,200))
               text.setFontColor('blue')
               paper1.add(text)
               startEventHandling()

class trasposeHandler(EventHandler):
     def __init__(self, paper, A, B):
          EventHandler.__init__(self)
          self.paper = paper
          self.A = A
          self.B = B
          
     def handle(self,event):
          if event.getDescription() == "mouse click":
               paper3 = Canvas(400,400,"linen", "Matrix Addition")
               r = Traspose(self.A)
               result = display(r)
               trasposeA = Text('Traspose A', 26, Point(100,100))
               text = Text(result, 26, Point(100,200))
               text.setFontColor('blue')
               paper3.add(text)
               paper3.add(trasposeA)

               r1 = Traspose(self.B)
               result1 = display(r1)
               trasposeB = Text('Traspose B', 26, Point(300,100))
               text1 = Text(result1, 26, Point(300,200))
               text1.setFontColor('blue')
               paper3.add(text1)
               paper3.add(trasposeB)
               
               
               startEventHandling()
          
class matrixMultiHandler(EventHandler):
     def __init__(self, paper, A, B):
          EventHandler.__init__(self)
          self.paper = paper
          self.A = A
          self.B = B
          
     def handle(self,event):
          if event.getDescription() == "mouse click":
               paper2 = Canvas(400,400,"linen", "Matrix Addition")
               r = matrixMult(self.A, self.B)
               result = display(r)
               text = Text(result, 26, Point(200,200))
               text.setFontColor('blue')
               paper2.add(text)
               startEventHandling()
               
def processData(data):
    rows = len(data)
    
    print('number of lines is',rows)
    
    A=list()

    cols=0
    for r in range(rows):
        line=data[r].split() # split by white space, store is a list

        if r == 0: # getting the number of elements in each string of the list
            cols=len(line)
            print('number of elements in each line is ',cols)

        if len(line) != cols:
            print('Warning: line %d:'%(cols+1))

            raise ValueError('number of elements in this line is different from the lines above')

        # use list comprehension to convert each element to integer
        line_int=[int(elem) for elem in line]
            
        # appent the list of integers to list A as a next element of list A
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

def matrixAddition(A, B):

    r = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])):
            temp.append(A[i][j] + B[i][j])

        r.append(temp)


    return r

def matrixMult(A, B):

    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    print (C)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C

def Traspose(A):

    return [[A[j][i] for j in range(0, len(A[i]))] for i in range(0, len(A))]

def main():

     while True:

        fmatrix = input('Please, input the name of the file with the first matrix:')
        Smatrix = input('Please, input the name of the file with the second matrix:')
        finalMatrix = input('Please, input the name of the file where you want to store the result:')
        
        try:
            f=open(fmatrix)
            f1=open(Smatrix)
            f2 = open(finalMatrix, 'w')
            break
        except ValueError:
            print('cannot open file',fmatrix, Smatrix)
            

     print('File %s is opened successfully!'%fmatrix)
     print('File %s is opened successfully!'%Smatrix)


     data = f.readlines()
     data1 = f1.readlines()


     A =processData(data)
     B =processData(data1)
     M1 = display(A)
     M2 = display(B)


     width = 800
     height = 600
     paper = Canvas(width,height,"white","Operations with Matrices")

     welcome = Text('Press any button to compute the operation', 20, Point(400,11))
     paper.add(welcome)
     #-------------------------------------------------------------#
     button1 = Button("Addition",Point(width//8,height//8))
     button1.setFontSize(18)
     button1.setFillColor("linen")
     paper.add(button1)
     button1.addHandler(matrixAddHandler(paper, A, B))
     #-------------------------------------------------------------#
     button2 = Button("Multiplication",Point(width//2,height//8))
     button2.setFontSize(16)
     button2.setFillColor("linen")
     paper.add(button2)
     button2.addHandler(matrixMultiHandler(paper, A, B))
     #-------------------------------------------------------------#
     button3 = Button("Traspose",Point(width-100,height//8))
     button3.setFontSize(18)
     button3.setFillColor("linen")
     paper.add(button3)
     button3.addHandler(trasposeHandler(paper, A, B))
     #-------------------------------------------------------------#
     buttonE = Button("EXIT",Point(width-100,height-50))
     buttonE.setFontSize(18)
     buttonE.setFillColor("orange")
     paper.add(buttonE)
     buttonE.addHandler(exitButtonHandler(paper))
     #-------------------------------------------------------------#
     title = Text('Matrix A ', 20, Point(250, 300))
     text = Text(M1, 26, Point(250,400))
     text.setFontColor('black')
     title.setFontColor('red')
     paper.add(title)
     paper.add(text)
     title1 = Text('Matrix B ', 20, Point(500, 300))
     text1 = Text(M2, 26, Point(500, 400))
     text1.setFontColor('black')
     title1.setFontColor('red')
     paper.add(text1)
     paper.add(title1)


     startEventHandling()

main()


