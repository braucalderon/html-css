import time

def take_words():
    print('This program will remove any desired words entered by \nthe user \n\n< Only LowerCase Characters > ')
       
    while True:
        
        w=input('\nInput a sentence: ').split(',')
        w=list(w) 
        #print(w)
        
        
        t=input('\nTo remove any word from the sentence \nenter < Y > otherwise enter < N >: ')
        s=' '
        if t == 'n' or t == 'no':
            print ("\nInput without any changes: ", ', '.join(w))
            time.sleep(1)
            print ("\nThank you for using the program")
            time.sleep(3)
            quit()
            
        while True:
            
            u=input('\nInput the desire word to be removed: ').split()
            u=list(u)
            #print(u)
               
        
            for i in w:
               # print(i)
                if i in u:
                    w.remove(i)        
                    
                    
            
            print ("\nThis is your new sentence: ",s.join(w))


          
            r=input('\nTo remove another word from the sentence \nenter < Y > otherwise < N >to quit the program: ')
            

                
                
            if r == 'n' or r == 'no':
                print ("\nThank you for using the program")
                time.sleep(2)
                quit()
            

        

take_words()
        

    

    




    
