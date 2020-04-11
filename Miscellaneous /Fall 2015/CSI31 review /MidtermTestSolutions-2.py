# Solutions to midterm.
# RUN IT to see answers


print("QUESTION 1")
x, y = 9, 7
x = y
y = x
print("x = ", x, " y = ", y)


print("\n\nQUESTION 2")
myString = "u 2 r happy?"
print(myString[4])
print(myString[:7])
print(myString[7:] + myString[2])

print("\n\nQUESTION 3")
x = 5
y = -2
if x < y:
    x = x + 1
elif x == -1:
    y = y + 1
elif x - 6 > y:
    y = y + 5
else:
    y = y - 5

print("x = ",x," y = ", y)


print("\n\nQUESTION 4")
my_val = 8
while my_val < 15:
    print(my_val)
    my_val = my_val + 3

print("\n\nQUESTION 5")
var82 = 100
print("Initial value of var82 = ", var82)
var82 = var82 + 3
print("New value of var82 = ", var82)



print("\n\nQUESTION 6")
def Find_Difference(a,b):
    return abs(a - b)

print("Difference of 3 and 8:", Find_Difference(3, 8)) # an example



print("\n\nQUESTION 7")
age = 19
minors, adults, seniors = 0, 0, 0
if age < 18:
    minors = minors + 1
elif age >= 18 and age <= 64:
    adults = adults + 1
elif age >= 65:
    seniors = seniors + 1

print(age, minors, adults, seniors)


print("\n\nQUESTION 8")
phrase = input("Give me a phrase: ")
count = 0
for ch in phrase:
    if ch == "x" or ch == "X":
        count = count + 1
print(count)


print("\n\nQUESTION 9")
def sum_odds(a,b):
    total = 0
    for k in range(a, b+1):
        if k % 2 == 1:
            total = total + k
    return total
print(sum_odds(4, 11))

print("\n\nQUESTION 10")
def isSecondSmallest(M, a, b):
    if (a < M and M < b) or (b < M and M < a):
        return True
    else:
        return False

def FindSecondSmallest(x, y, z):
    if isSecondSmallest(x, y, z):
        return x
    if isSecondSmallest(y, x, z):
        return y
    return z

print(FindSecondSmallest(4, 9, 3))



print("\n\nQUESTION 11")
import graphics
from graphics import *
win = GraphWin("my window", 100, 100)
center = win.getMouse()
C = Circle(Point(center.getX(), center.getY()), 10)
C.draw(win)
new_center = win.getMouse()
C.move(new_center.getX() - center.getX(), new_center.getY() - center.getY())


