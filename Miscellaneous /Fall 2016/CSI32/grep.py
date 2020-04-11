def grep():
    for line in open('internet.txt'):
        line = line.strip()
        if 'some' in line:
            print (line)
        
        
            
    
     
        
        

def main():
    

    
  
    if grep().readlines() > 0:
        print (grep())
    if grep().readlines() == 0:
        print ('n')
           
    
           
            
    
            

##    if grep() == False:
##        print('n')
       

main()
