toto = raw_input('Enter file name')

try:
    fhand = open('toto') 
except:
    print 'Incorrect Input:',toto
    exit()



