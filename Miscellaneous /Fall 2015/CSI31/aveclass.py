#Associate the average of the numbers from 1 to n
#(where n is a positive integer value)
#with the variable  avg.

n=eval(input("Enter number, "))
total=0.0
for k in range(n+1):
    total=total + k
print (total/n)

