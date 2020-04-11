# Exercise 4.35
import time

def lis_num():
    
    print ("\nThis program will generate a list of numbers using the method of \nlist comprehension")

    print ("\n< The user must input a number only >    \nEx: Input: 2, Ouput:[1.5, 2.5, ext]")

    while True:

        m=eval(input("\nPlease input the numbers to generate: "))
        
        l=[]
        for i in range(1,m+1):
            
            l.append(float(i/1.0 + 0.5))
        print("\nNumbers generated: ",l)


        time.sleep(1)
        m=input("\nTo generate more numbers enter < y > or < n >: ").lower()


        if m == 'n' or m == 'no':
            print ('\nThank you for using the program')
            time.sleep(1)
            quit()
        


        
            
        

lis_num()
        
