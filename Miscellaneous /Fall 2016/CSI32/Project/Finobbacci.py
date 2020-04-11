#Finobbacci

from cs1graphics import *
import time 



def fibonacci(n):

    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

p=[]
for i in range(1,9):
    p.append(fibonacci(i))

#print (p[3])

    

class Square(Rectangle):

    def __init__(self, width=25, height=25, center=Point(315,200)):
        Rectangle.__init__(self, width, height, center)

    def setWidth(self,width):
        self.setWidth()

    def setHeight(self, height):
        self.setHeight()

    def getWidth(self):
        return self.Width()

    def getHeight(self):
        return self.Height()

    

    
        
def main():
    
    paper=Canvas(500, 350,'white', 'Fibonacci')
    s=Square()
    time.sleep(1)
    s.setBorderColor('darkred')
    s.setBorderWidth(2)
    paper.add(s)
    s=Text(str(p[0]), 10)
    s.move(315,200)
    paper.add(s)

    time.sleep(1)
    s1=Square(25,25,Point(340,200))
    s1.setBorderColor('darkred')
    s1.setBorderWidth(2)
    paper.add(s1)
    s1=Text(str(p[1]), 10)
    s1.move(340,200)
    paper.add(s1)    

    time.sleep(1)
    s2=Square(50,50,Point(327,161))
    s2.setBorderColor('darkred')
    s2.setBorderWidth(2)
    paper.add(s2)
    s2=Text(str(p[2]),15)
    s2.move(327,161)
    paper.add(s2)

    time.sleep(1)
    s3=Square(145,77,Point(425,175))
    s3.setBorderColor('darkred')
    s3.setBorderWidth(2)
    paper.add(s3)
    s3=Text(str(p[3]), 25)
    s3.move(425,175)
    paper.add(s3)

    time.sleep(1)
    s4=Square(195,130,Point(400,280))
    s4.setBorderColor('darkred')
    s4.setBorderWidth(2)
    paper.add(s4)
    s4=Text(str(p[4]), 35)
    s4.move(400,280)
    paper.add(s4)

    time.sleep(1)
    s5=Square(130,209,Point(236,240))
    s5.setBorderColor('darkred')
    s5.setBorderWidth(2)
    paper.add(s5)
    s5=Text(str(p[5]), 45)
    s5.move(236,240)
    paper.add(s5)

    time.sleep(1)
    s6=Square(326,125,Point(334,70))
    s6.setBorderColor('darkred')
    s6.setBorderWidth(2)
    paper.add(s6)
    s6=Text(str(p[6]), 50)
    s6.move(334,70)
    paper.add(s6)

    time.sleep(1)    
    s7=Square(165,337,Point(85,176))
    s7.setBorderColor('darkred')
    s7.setBorderWidth(2)
    paper.add(s7)
    s7=Text(str(p[7]), 60)
    s7.move(85,176)
    paper.add(s7)

    time.sleep(1)
    s8=Square(450, 175,Point(265, 175))
    s8.setBorderColor('white')
    s8.setFillColor('white')
    paper.add(s8)
    s8=Text('Finobbacci Series', 35)
    s8.setFontColor('blue')
    s8.move(250, 175)
    paper.add(s8)
    


main()
    

    
