h=eval(input("Enter Number, "))
q=0
for i in range(1,h+1):
    
    if i < h:
        i=i**2
        q = q + i
print (q)
