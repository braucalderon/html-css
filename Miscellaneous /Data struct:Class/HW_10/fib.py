# fib.py

three = 0 # global value created outside of the function. 

def recFib(n):

        global three # global non-local variable to be called into the function 
        
        print("\nComputing Fib({})".format(n)) # prints the number to be computed
        if n == 3:      # counts the number to be computed 
                three += 1
                
        if n < 3:
                print("\nLeaving Fib({}), returning 1".format(n)) 
                return 1 # returns 1 for values 0 and 1 
        else:
                r = recFib(n-1) + recFib(n-2)
                print("\nLeaving Fib({}), returning {}".format(n,r))
                return r # returns values greater than 3 
                  


while True:
        
        n = int(input("Enter a non-negative integer to compute Fib: "))
        
        recFib(n) # calls the function 
        print("\nFibonacci (3) is computed {} time(s) in Finobacci ({})"
              .format(three, n)) # calls the glabal variable for 3 and # computed 
        
                
        Flag = input("\nPress F to quit, else any key: ")

        if Flag == "f": # breaks the out of the while loop if f is press
                break
        else:
                three = 0 # sets three to zero every time a new number computed 
    
    
    


