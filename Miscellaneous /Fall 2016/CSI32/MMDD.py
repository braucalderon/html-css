# Exer: Write a program that inputs a date and outputs how many days into the
# year it is
import time 
def mm():
    print ("This program will assist you in finding how many \ndays into the year for month and date entered")
    w=True
    while True:
        m=eval(input('Please enter the month first:  '))
        r=eval(input('Please enter the day of the month: '))

        total=0
        
        if m == 1 and r < 31:
            print (r)
            break
        else:
            if 
            print ('January does not have', r ,'days')
            break
        
        if m == 2 and r < 29:
            total=total+(31+r)
            print (total)
            break
        
        else:
            print ('Feabraury does not have',r,'days')
            break
        
        if m == 3 and r <= 31:
            total=total+(60+r)
            print(total)
        else:
            print ('March does not have', r, 'days')
            break

        if m == 4 and r <= 30:
            total=total+(91+r)
            print (total)
            break
        
        else:
            print ('April does not have', r, 'days')
            break

        if m == 5 and r <= 31:
            total=total+(121+r)
            print (total)
        else:
            print ('May does not have', r, 'days')
            break

        if m == 6 and r <= 30:
            total=total+(152+r)
            print (total)
        else:
            print ('June does not have', r, 'days')
            break

        if m == 7 and r <= 30:
            total=total+(182+r)
            print (total)
        else:
            print ('July does not have', r, 'days')
            break

        if m == 8 and r <= 31:
            total=total(212+r)
            print (total)
        else:
            print ('August does not have', r, 'days')
            break

        if m == 9 and r <= 30:
            total=total+(243+r)
            print (total)
        else:
            print ('September does not have', r, 'days')
            break

        if m == 10 and r <= 31:
            total=toal+(273+r)
            print (total)
        else:
            print ('October does not have', r, 'days')
            break

        if m == 11 and r <= 30:
            total=total+(304+r)
            print(total)
        else:
            print ('November does not have', r, 'days')
            break

        if m == 12 and r <= 31:
            total=total+(334+r)
            print (total)
        else:
            print ('December does not have', r, 'days')
            break

    w=input('To continue press < y > otherwise enter < n >: ')
    if w == 'y' or w == 'yes':
        return True
    else:
        quit () 
            


        

            
                
                  
    

mm()
