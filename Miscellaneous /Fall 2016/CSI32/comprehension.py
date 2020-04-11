def comprehension():
    
    n=eval(input('Input the number: '))
    l=[i/(i+1)**3 for i in range (1,n,2)]

    print (l)

comprehension()

