##def main():
##    n=eval(input("Enter a positive number "))
##    
##    for i in range(n + 1):
##        for j in range (n + 1):
##            print (i, 'x', j, '=', i*j, end = 'it')
##    print
##
##main 

def main():
    
    
    result=[(-1)**i * i*i for i in range(1,10)]
    print (result)

main()
        
