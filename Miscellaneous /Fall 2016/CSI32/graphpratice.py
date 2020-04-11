#Graph Practice 

from cs1graphics import * 

paper=Canvas(300,200, 'skyBlue', 'My World')

sun=Circle(30, Point(250,50))
sun.setFillColor('yellow')
paper.add(sun)

facade = Square(60, Point(140,130))
facade.setFillColor('white')
paper.add(facade)

chimney = Rectangle(15,28, Point(155,85))
chimney.setFillColor('red')
chimney.setBorderColor('red')
paper.add(chimney)

tree=Polygon(Point(50,70), Point(30,140), Point(70,140))
tree.setFillColor('darkGreen')
paper.add(tree)

car=Layer()
tire1= Circle(10,Point(-20, -10))
tire1.setFillColor('Black')
car.add(tire1)

tire2=Circle(10,Point(20,-10))
tire2.setFillColor('black')
car.add(tire2)

body=Rectangle(70, 30, Point(0,-25))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)
