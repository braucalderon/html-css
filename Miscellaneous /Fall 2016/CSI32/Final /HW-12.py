# Exercise 8.6
#Page 293

#Assume that the file people.txt contains one or more lines
#where each line is the name of a famous person followed by
#the year in which he or she was born. 


import time

def main():

    while True:
        filename = input('Please enter the file name: ')
        try:
            fname = open(filename)
            break
        except IOError:
            print('\nInvalid file input, try again!')
            
    
    
    
        
    while True:
        
        year=eval(input('\nPlease enter the year: '))
        try:
            if year > 0: 
                break
            else:
                print('\nThe birth year must be positive')
            
            
        except:
            year
            
           
            
    y=[]
    number=[]
    for line in fname.readlines():
        #print(line)
        line=line.split()
        y.append(line[-1:])
        #print(y)
        if str(year) in line:
            print('\nIndivual found in file:',' '.join(map(str,line[:-1]))) #get rid off the brackets
            break
    if str(year) not in line:
        print('\nBirth year not found in the file')
        time.sleep(1)
        quit()
    
    new=[]
    for i in y:
        new+=i
    
    
    if (('877') == str(year)):
        print('\nThis is the oldest individual in the file')
        
    else:
        print('\nThis is not the oldest individual in the file')
        
        

            
    
  
# I could make the code below to work to find the min value and add the value in the
# ' if 'statement

##    l=map(int,total)
##    x=min(l)
##    new.append(str(x))
##    print (new)

    
            
            


    
    
    
main()
