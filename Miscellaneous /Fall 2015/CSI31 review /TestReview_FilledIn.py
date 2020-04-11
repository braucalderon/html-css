################
# Writing Code #
################

# 1
# Write a program that swaps the values in
# variables A and B.
A, B = B, A


# 2
# Write a function that takes in 5 numbers
# as input and outputs their average.
def average(a,b,c,d,e):
    avg = (a + b + c + d + e) / 5
    return avg


# 3
# Write a program that prompts the user
# for two numerical inputs (L and W)
# and prints out the area of a rectangle
# with length L and width W.
L = eval(input("Enter the length:"))
W = eval(input("Enter the width:"))
Area = L*W
print("The area is: ", Area)

# OR
L, W = eval(input("Lenght and Width? "))
print("Area is: ", L*W)


# 4
# Do the last program again, but do it so
# that it complains if either the length
# or width is not a valid number.
L, W = eval(input("Lenght and Width? "))
if L <= 0 or W <=0:
    print("Not valid dimensions!")
else:
    print("Area is: ", L*W)


# 5
# One pound is 0.45kg.
# 1) Write a function that takes a number
#    as input and outputs its conversion
#    to kg.
# 2) Write a function that takes a number
#    as input and outputs its conversion
#    to pounds
# YOU PRACTICE!


# 6
# Write a program that opens up a graphics
# window and then draws a circle and a
# rectangle inside the circle (any sizes
# are fine, as long as the rectangle is
# inside the circle, not touching the
# circle).
def shapes():
    import graphics
    from graphics import *
    win = GraphWin("Practice6",100,100)
    win.setCoords(0,0,10,10)
    Cr = Circle(Point(5,5),4)
    Cr.draw(win)
    Rt = Rectangle(Point(5,5),Point(6,7))
    Rt.draw(win)


# 7
# Write a program that does the following:
# - It gets a mouse click from the user
# - It draws a circle with the center
#     where the user clicked
# - Then it gets another mouse click and
#     moves the circle so that its new
#     center is at that mouse click.


# 8
# Write a function that takes 3 numbers as
# input and outputs the minimum of the 3
# numbers


# 9
# Write a function that takes 3 positive
# numbers as input and outputs the middle
# number if the 3 numbers are distinct,
# and outputs -1 if they are not distinct


# 10
# Write a function that takes a positive
# integer n as input, and outputs the number
# of positive even integers less than n.
def NumEven(n):
    count = 0
    for k in range(1,n):
        if k % 2 == 0:
            count = count + 1
    
    return count
# QUESTION: Do this program without a loop

# 11
# Write a function that takes a positive
# integer n as input, and outputs the number
# of positive even integers less than n, and
# the number of positive odd integers
# less than n.


# 12
# Write a function that takes a positive
# integer n as input, and ouputs the sum
# of the positive even integers less than n.


# 13
# Write a function that takes a positive
# integer n as input, and ouputs the sum
# of the positive odd integers less than n.


# 14
# Write a program that takes a sentence
# as user input and then prints out the
# number of 4-letter words in the sentence.


# 15
# Write a function that takes a list of
# numbers as input and returns the sum of
# the numbers in the list.


# 16
# Ch.7- Programming Exercise #1


#################
## Reading Code #
#################

# How does Python evaluate each of the
# following lines:
9 % 4
12 % 4
9 // 4
9 / 4
"34" + "10"


# Suppose S is the string "BCC Math".
# How does Python evaluate the following
# expressions
S = "BCC Math"
S[2]
S[2:6]
S[2:]
S[:2]


# What does the following code print
k = -5
if k > 0:
    print(k)
elif k < -5:
    print(k*2)
elif k == -4.9:
    print(k+2)
else:
    print(k - 1)


# What does the following program print?
for k in range(2,6):
    print(k+5)


# What does the following program print?
for k in [2,1,9]:
    print(k**2)


# What is the value of k after running the
# following program?
k = 2
for ch in "Hi Kid":
    k = k + 2


# What does the following code print
test_val = 10
while test_val > 2:
    print(test_val)
    test_val = test_val - 2
print("done")


# What does the following code print
test_val = 10
while test_val > 2:
    print(test_val)
    test_val = test_val - 2
    print("done")

# What does the following code print
test_val = 10
while test_val < 2:
    print(test_val)
    test_val = test_val - 2
print("done")
