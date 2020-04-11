# Exersice 8.11


# There is a standard Unix tool named grep,that in simplest form performs the
# following task.For a given input file and a given search term, print out
# only those lines of the file that contain the given search term.
# Implement such a program yourself.

print("\nThis program will help you to find word(s) in any the file")

def grep_file(fname,w):
        flag=0   
        for line in fname:
            if w in line:
                flag+= 1
                print('Phrase with', '"',w,'":\n', line)
        
        if flag == 0:
                print('"',w,'"'," was not found in the file")
            
                      

def main():
    
    while True:
        filename = input('Please enter the file name: ')
        try:
            fname = open(filename)
            break
        except IOError:
            print('\nInvalid file input, try again!')

    
    
    
    w=input('Search word: ')

    (grep_file(fname,w)) 

    
##    if grep_file(fname,w) == None:
##            print ('\nUnable to find the word','"',w.upper(),'"','in the file')
##            break
    
    
   
        
##    if grep_file(fname,w) != None: 
##        print (grep_file(fname,w))
##              
##    if grep_file(fname,w) == None:
##        print ('\nUnable to find the word','"',w.upper(),'"','in the file')
        
        
        
    
    
    

main()


