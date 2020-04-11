# Exer: Write a program that inputs a date and outputs how many days into the
# year it is
import time 
def mm():
    print ("\nThis program will assist you in finding how many days each date has \ninto the calendar year\n")
    print ('\nThe program will let you know if any input is incorrectly, base on the \nprogram capability')
    w='yes'
    
    while w[0] == 'y':
        print('\nThe month must be entered as a single digit Example: Jan = 1, Feb = 2')
        m=eval(input('\nPlease enter the month in the following format (M) or (MM):  '))
             
        r=eval(input('\nPlease enter the day of the month: '))

        j=31
        f=29
        mar=31
        ap=30
        may=31
        jun=30
        jul=30
        aug=31
        sep=30
        octo=31
        nov=30
        dec=31
        
        if m > 12:
            print ('\nThe calenday year does not', m, 'of months')
            print ('\nTry again')
            
        time.sleep(1)    
        if m == 1 and r > j:
            print ('January does not have', r, 'days')
            print ('\nTry again')
        elif m == 1 and r <= j:
            print ('Day', r,'of January is',r,'days into the year')
            
        
        
        if m == 2 and r > f:
            print ('Febreaury does not have', r, 'days')
            print ('\nTry again')
        elif m == 2 and r <= f:
            print ('Day',r, 'of Febreaury is',(r+j),'days into the year')
            

            
        if m == 3 and r > mar:
            print ('March does not have', r, 'days')
            print ('\nTry again')
        elif m == 3 and r <= mar:
            print ('Day', r, 'of March is',(j+f+r), 'days into the year')
            

        
        if m == 4 and r > ap:
            print ('April does not have', r, 'days')
            print ('\nTry again')
        elif m ==4 and r <= ap:
            print ('Day', r, 'of April is',(j+f+mar+r), 'days into the year')
            

        
        if m == 5 and r > may:
            print ('May does not have', r, 'days')
            print ('\nTry again')
        elif m == 5 and r <= may:
            print ('Day', r, 'of April is',(j+f+mar+ap+r), 'days into the year')
            

        
        if m == 6 and r > jun:
            print ('June does not have', r, 'days')
            print ('\nTry again')
        elif m == 6 and r <= jun:
            print ('Day', r, 'of June is',(j+f+mar+ap+may+r), 'days into the year')
            

        
        if m == 7 and r > jul:
            print ('July does not have', r, 'days')
            print ('\nTry again')
        elif m == 7 and r <= jul:
            print ('Day', r, 'of July is',(j+f+mar+ap+may+jun+r), 'days into the year')
            

        
        if m == 8 and r > aug:
            print ('August does not have', r, 'days')
            print ('\nTry again')
        elif m == 8 and r <= aug:
            print ('Day', r, 'of August is',(j+f+mar+ap+may+jun+jul+r), 'days into the year')
            

        
        if m == 9 and r > sep:
            print ('September does not have', r, 'days')
            print ('\nTry again')
        elif m == 9 and r <= sep:
            print ('Day', r, 'of September is',(j+f+mar+ap+may+jun+jul+aug+r), 'days into the year')
            

        
        if m == 10 and r > octo:
            print ('October does not have', r, 'days')
            print ('\nTry again')
        elif m == 10 and r <= octo:
            print ('Day', r, 'of October is', (j+f+mar+ap+may+jun+jul+aug+sep+r), 'days into the year')
            

        
        if m == 11 and r > nov:
            print ('November does not have', r, 'days')
            print ('\nTry again')
        elif m == 11 and r <= nov:
            print ('Day', r, 'of November is',(j+f+mar+ap+may+jun+jul+aug+sep+octo+r), 'days into the year')
            

        
        if m == 12 and r > dec:
            print ('December does not have', r, 'days')
            print ('\nTry again')
        elif m == 12 and r <= dec:
            print ('Day', r, 'of December is',(j+f+mar+ap+may+jun+jul+aug+sep+octo+nov+r), 'days into the year')



            
        time.sleep(1)
        w=input('\nTo continue please enter < Y > otherwise enter to end it < N >:  ').lower()
 
        
        if w[0] == 'n' or w[0] == 'N' or w[0] == 'NO':
        
            print ('\nThank you for using the program')
            time.sleep(1)
            quit()
            
        elif w[0] != 'y':
            print ('\nWrong input')
            print ('Remeber < y > or < n >')
            w=input('\nTo continue please enter < Y > otherwise enter to end it < N >:  ').lower()
         
        if w[0] != 'y':
            print('\nYou have exited the program')
            time.sleep(1)
            quit()
    
            
mm()
                
                

    
