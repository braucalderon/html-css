# Ex: 5.30 Write a function with a signature cheerlead(word)that prints a typical
# cheer.
import time

def cheer():
    print ('\nCheer program')

    print ('\nOhh well, here we go')

    while True:
        while True:

            m=input("\nPress < y > to start or < n > to quit: ").lower()

            if m == 'y' or m == 'yes':
                break

            if m == 'n' or m == 'no':
                print ('\nBye for now')
                time.sleep(1)
                quit()
            
            if m != 'y' or m != 'yes':
                print ('\nRepeat again')
                m=input ('\nJust press < y > or < n >: ').lower()    
            if m == 'y' or m == 'yes':
                print ('Thank you')
                break
            if m == 'n' or m == 'no':
                print ('\nCome back when you are ready \n\nBye for now')
                time.sleep(1)
                quit()
            
            
            if m != 'y'or m != 'yes':
                print ('\nLast chance')
                m=input ('\nOne more try, JUST < y > or < n >: ').lower()
            if m == 'y' or m == 'yes':
                print ('Thank you')
                break
            if m == 'n' or m == 'no':
                print ('\nCome back when you are ready \n\nBye for now')
                time.sleep(1)
                quit()
            
            if m != 'y' or m != 'yes':
                print ('\nOhhh well, You are not a team player')
                time.sleep(1)
                quit ()

            


        if m == 'y' or m == 'yes':
            print("\nNow, Let's start by you giving me a phrase")

            time.sleep(1)
            l=input('\nInput a phrase to start:  ')
            mylist=list(l)

        
        while True:
            new=[]
            
            v=['f','h','l','m','n','y','s','x','a','e','o','u', 'i', 'r']
            for word in mylist:
                new.append(word)
              
            for i in new:
                
                if i not in v:
                    time.sleep(1)
                    print ('\nGimme a',i.upper())
                    
                if i in v:
                    time.sleep(1)
                    print ('\nGimme an',i.upper())
                    
                    
                
            t=input("\nWhat's that spell? ").lower()
            r=list(t)
            w=[]
            for i in r:
                w.append(i)
           
                
            if w == new:
                print('\nGreat')
                break
                    
            if w != new:
                print("\nLet's try again") 
                u=input("\nWhat's that spell one more time? ").lower()
                y=list(u)
                f=[]
            for i in y:
                f.append(i)
            
            if f == new:
                print ('\nGreat')
                break
            else:
                print ("\nohh, well, let's start again")
                break
            
        time.sleep(1)    
        h=input('\nOne more thing, if you want to quit, press < n > \notherwise press any < keyboard >: ').lower()
        if h == 'n' or h == 'no':
            print ('\nBye')
            time.sleep(1)
            quit()
            

        
        
    
        
        
        
            
        
        
        
            
            
            
             
                
                
        
        
        



cheer()
