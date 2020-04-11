import math
import time

def main():

    print('The program will evaluate terms of this \nseries by using pi(1/1)-(1/3)+(1/5)- ...\n')

    time.sleep(1)
    input('Press < Any Key > to start')
    
    
    
    
    m='yes'
    while m[0]=='y':
    #m[0]:y=0, e=1, s=2
        n=eval(input("Enter the number of terms to be calculated: "))

        
        total=0
        #total holds the first result if n > 1
        m=4
        
        for i in range(n):
        #if n > 1, then will not count the last term
        #Ex: n=1 will run 0 but not 1
            
            total = total + m *  (-1) ** i * 1/(2*i+1)
            #total will add the first term if n > 1 to the next one
            
        print ('\nThe sum of the term(s) using pi is:', total)
        
        time.sleep(1)        
        m=input('\nIf you want to calculate another set of terms enter < y > \notherwise < n > to exit the program\n')

    if m[0]=='n' or 'no':
        print ('You have exited the program')
    time.sleep(1)

    quit()
    
main()

    
