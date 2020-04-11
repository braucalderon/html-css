#Chapter 11
# question 11

def count():
    
    file =input('Please your source of file:   ')
    infile = open(file,"r")
    oldfile=file.split()
    
    for item in oldfile:
        if len(item)==4:
            newfile=item
        print(newfile)


#I dont know how to save a new file. 
            
            

count()
