#problem 1. topic, Chap 6

#write a function to count the number of perfect squeares
#less than the given input: Use a for loop that goes from 1 to h
#calling a function to check which values are prefect.
import math

def perfectsquare (h):
    return math.sqrt(x)==int(math.sqrt(x)) and x != 0

def countperfect (h):
    
    count = 0
    for k in range (h):
        if perfectsquare(k):
            count = count + 1
    return count 
     
