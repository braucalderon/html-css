Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Oct 29, 2015
>>> 

>>> import graphics
>>> from graphics import *
>>> C1 = Circle(Point(3,5), 10)
>>> C2 = Circle(Point(13,15), 20)
>>> C1.getCenter()
<graphics.Point object at 0x02E346D0>
>>> C1.getRadius()
10
>>> C2.getRadius()
20
>>> p = C1.getCenter()
>>> p.getX()
3.0
>>> p1 = p
>>> p1.getX()
3.0
>>> p2 = C2.getCenter()
>>> p2.getX()
13.0
>>> C1.move(100,100)
>>> p1.getX()
3.0
>>> p1 = C1.getCenter()
>>> p1.getX()
103.0
>>> p2 = C2.getCenter()
>>> p2.getX()
13.0
>>> ================================ RESTART ================================
>>> 
>>> die1 = Die(6)
>>> die2 = Die(15)
>>> die1.sd
6
>>> die2.sd
15
>>> die1.value
1
>>> die2.value
1
>>> die2.roll()
>>> die2.getValue()
2
>>> die2.roll()
>>> die2.getValue()
6
>>> ================================ RESTART ================================
>>> 
>>> student1 = BCC_student("Daniel", 3.4, 54, 9)
>>> student2 = BCC_student("Kerry", 4.0, 75, 3)
>>> student1.hasGraduated(60)
False
>>> student2.hasGraduated(60)
True
>>> ================================ RESTART ================================
>>> 
QUESTION 1
x =  7  y =  7


QUESTION 2
r
u 2 r h
appy?2


QUESTION 3
x =  5  y =  3


QUESTION 4
8
11
14


QUESTION 5
Initial value of var82 =  100
New value of var82 =  103


QUESTION 6
Difference of 3 and 8: 5


QUESTION 7
19 0 1 0


QUESTION 8
Give me a phrase: hhdscxx9f xX
4


QUESTION 9
32


QUESTION 10
4


QUESTION 11

>>> sent = "  g xX f cx ,xx"
>>> sent.count("x")
4
>>> sent.count("X")
1
>>> x, y, z = 5, 2, 20
>>> if y < x < z:
	middle = x

	
>>> middle
5
>>> x, y, z = 5, 20, 2
>>> if y < x < z:
	middle = x

	
>>> if y < x < z:
	new_middle = x

	
>>> new_middle
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    new_middle
NameError: name 'new_middle' is not defined
>>> if y < x < z or z < x < y:
	middle = x

	
>>> 
