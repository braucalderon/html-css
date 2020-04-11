# HW 6 Write a program that calculates the distance between two points.

import math 

def points():
    
    print('\nFormat to enter the points x,y,x,y')
    print('\nValues X2 not greater than 30 and Y2 not greater than 20')
    print('X1 and Y1 values greater than 0')
    while True :
        
        try:
            
            m=eval(input('\nEnter two points to calculate the distance:  '))
            p = list(m) # convert it into a list

            # assign the values of m into x1, y1, x2, y2
            x1=p[0]
            y1=p[1]
            x2=p[2]
            y2=p[3]


            
            if len(p) == 4 and  x2 <= 30 and y2 <= 20 and x1 >= 0 and y1 >= 0: 
                v=(((x2-x1)**2) + ((y2-y1)**2))
                print ('\nThe distance between the two points is: ',math.sqrt(v))
                break
            else: 
                print ("\nCheck your input. Someting looks out of place, Check the instructions.")
        
        except IndexError:
            print ('\nYou are missing one or few points in your input, check your input')
        except NameError:
            print ('\nYou are calculating numbers, not the letters of the alphabet')
        except SyntaxError:
            print ('\nPay more attention to your input, Ex: 3.5.6 or &*$^#%. not allowed')
        except TypeError:
            print ('\nNo way you will calculate the distance with that input')
        
    print ('\nThank you for using the program')
    

points()
