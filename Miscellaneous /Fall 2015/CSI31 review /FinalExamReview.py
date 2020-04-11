################
# Writing Code #
################




# 1
# Write a program that prompts the user
# for one numerical inputs (r)
# and prints out the EXACT and APPROXIMATE area
# of the circle with radius r.  For the exact,
# use the string "pi" to represent the number pi.




# 2
# Do the last program again, but do it so
# that it complains if the radius is not
# a valid number, and keeps asking the user
# for input till a valid number is input.




# 3
# One pound is 0.45kg.
# 1) Write a function that takes a number
#    as input and outputs its conversion
#    to kg.
Formula
1 / 2.2 = 0.45kg
pounds x 0.45 one kg = kg 

# 2) Write a function that takes a number
#    as input and outputs its conversion
#    to pounds

# 3) Make a main() function which calls
#    these functions at enough places to
#    constitute a reasonable test of the functions
# (Test Fuction)


# 4
# Do the last program, but make it a universal
# "unit converter", so it takes in how many of one
# thing convert to another


# 5
# Write a program that does the following:
# - It gets a mouse click from the user
# - It draws a square with the center
#     where the user clicked
# - Then it gets another mouse click and
#     moves the square so that its new
#     center is at that mouse click.


# 6
# Write a program that takes input from the
# user until "Enter" is hit with no number.
# The program outputs the value of the
# largest and smallest number inputed.


# 7
# Write a program that takes input from the
# user until "Enter" is hit input
# Assume each input is a word.
# Print out the words in alphabetic order.

# 8 TRY THIS!
# Write a program that takes input from the
# user until "Enter" is hit input
# Assume each input is an integer and at least one
# input is zero.
# Output the following statistics:
# - How many negative numbers?
# - How many zeros?
# - How many positive numbers?
# Note: Do this using list methods and NO loops.



# 9
# Write a function that takes a list as input
# and outputs the sum of the squares of the entries
# in the list.


# 10
# Write a program that creates a list
# of 26 tuples, where each tuple is
# the pair (i,l) where "i" is a number
# between 1 and 26 (inclusive) and
# l is letter i in the alphabet.

# 11 TRY THIS!
# Write a program that creates a list
# of triples, where the entry in each
# triple ranges from 2 to 4 (inclusive).





# 12
# Write a program that takes a sentence
# as user input and then prints out the
# number of 4-letter words in the sentence.


# 13
# Write a class for a classroom object
# which keeps track of:
#   - the teacher
#   - all students enrolled in the course
#   - which students are present
#   - which students are absent
# It should methods for modifying the data and
# aquiring the data.



#################
## Reading Code #
#################


#
print("*****************\nREADING PROBLEM 1")
x = 77
S = "BCC Math"
print(S[2:5] + str(x) + S[:3])


#
print("*****************\n\nREADING PROBLEM 2")
L = [2,9, 2,1]
X = L
X[2] = 0
print(L)


print("*****************\n\nREADING PROBLEM 3")
for (x,y) in [(2,3),(1,-1),(9,0)]:
    print(x + y)



print("*****************\n\nREADING PROBLEM 4")
for x in range(3):
    for y in range(2,4):
        print(x,y)
# Modify the above code so that
# it prints out
# "point 1 is: (0,2)"
# "point 2 is: ..."
# ETC.


#
print("*****************\n\nREADING PROBLEM 5")
class Silly:
    def __init__(self,x, X):
        self.v = x
        self.w = x + 2*X

    def __str__(self):
        return "v = " + str(self.v) + "; and w = " + str(self.w)

    def change(self,a,B):
        self.v = 2*a
        self.w = self.v + B

s = []
for (a,b) in [(2,4),(3,3),(0,1)]:
    next = Silly(a,b)
    s.append(next)

def printList(L):
    for l in L:
        print(l)

printList(s)
s[1].change(1, 3)
s[2].change(0.5, 0)
printList(s)







