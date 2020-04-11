# 1
# Write a program that prompts the user
# for one numerical inputs (r)
# and prints out the EXACT and APPROXIMATE area
# of the circle with radius r.  For the exact,
# use the string "pi" to represent the number pi.

import math
from math import pi

r = eval(input("Give me a radius: "))
print("Exact value = ",r**2,"pi")
print("Approx value = ", r**2 * math.pi)

# 2
# Do the last program again, but do it so
# that it complains if the radius is not
# a valid number, and keeps asking the user
# for input till a valid number is input.

r = eval(input("Give me a radius: "))
while r <= 0:
    print("Invalid input!")
    r = eval(input("Give me a radius: "))

print("Exact value = ",r**2,"pi")
print("Approx value = ", r**2 * pi)

# 6
# Write a program that takes input from the
# user until "Enter" is hit with no number.
# The program outputs the value of the
# largest and smallest number inputed.

L = []
x = input("Next number: ")
while x != '':
    L.append(eval(x))
    x = input("Next number: ")

print("Max = ", max(L))
print("Min = ", min(L))

# 7
# Write a program that takes input from the
# user until "Enter" is hit input
# Assume each input is a word.
# Print out the words in alphabetic order.

L = []
x = input("Next word: ")
while x != '':
    L.append(x)
    x = input("Next word: ")

L.sort()
print(L)


# 9.1
# Write a function that takes a list as input
# and outputs the list with each entry squared.
# Don't change the inputed list

def squareNotModify(L):
    sqL = []
    for i in L:
        sqL.append(i**2)
    
    return sqL

# 9.2
# Write a function that takes a list as input
# and outputs nothing.
# But it changes the inputed list so
# that each entry squared.

def squareModify(L):
    for i in range(len(L)):
        L[i] = L[i]**2

# Another try

def squareAnotherTry(L):
    sqL = []
    for i in L:
        sqL.append(i**2)
    
    L = sqL


# 9.5
# Modify the above code so that
# it prints out
# "point 1 is: (0,2)"
# "point 2 is: ..."
# ETC.

k = 0
for x in range(3):
    for y in range(2,4):
        k = k + 1
        print("Point", k, " is: ",x,y)

# 10
# Write a program that creates a list
# of 26 tuples, where each tuple is
# the pair (i,l) where "i" is a number
# between 1 and 26 (inclusive) and
# l is letter i in the alphabet.

myL = []
for i in range(26):
    myL.append((i+1,chr(ord('a')+i)))


# 11 
# Write a program that creates a list
# of triples, where the entry in each
# triple ranges from 2 to 4 (inclusive).

L = []
for x in range(2,5):
    for y in range(2,5):
        for z in range(2,5):
            L.append([x,y,z])

print(L)
            
  

# 13
# Write a class for a classroom object
# which keeps track of:
#   - the teacher
#   - all students enrolled in the course
#   - which students are present
#   - which students are absent
# It should methods for modifying the data and
# aquiring the data.

class Classroom:
    def __init__(self, teacher):
        self.teacher = teacher
        self.allStudents =[]
        self.presentStudents = []
        self.absentStudents = [] # maybe don't use?

    def getStudents(self):
        return self.allStudents

    def getPresentStudents(self):
        return self.presentStudents

    def getAbsentStudents(self):
        return self.absentStudents

    def addStudent(self, studentName):
        self.allStudents.append(studentName)
        self.absentStudents.append(studentName)

    def markPresent(self, studentName):
        if studentName in self.allStudents:
            self.presentStudents.append(studentName)
            if studentName in self.absentStudents:
                self.absentStudents.remove(studentName)

    def markAbsent(self, studentName):
        if studentName in self.allStudents:
            self.absentStudents.append(studentName)
            if studentName in self.presentStudents:
                self.presentStudents.remove(studentName)





