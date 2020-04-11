# HW 4
import time

def space():
    
    print ("This program will recognize numerical strings and converte them into integers. \nEx: ['gft',123]\n")
    while True:
        
        w=input("\nPlease enter a sentence may include numbers: ").split(',')
        p=list(w)
       
        #print(w)
        k=[]
        
        for i in p:
        
            if str(i).isdigit() > 0:
                k.append(int(i))

            else:
                k.append(i)
        print ('The following is the input: ',k)
        break
    print('\nYou had exited the program')
    time.sleep(3)
    quit()
            
        
            
        

space()
    
