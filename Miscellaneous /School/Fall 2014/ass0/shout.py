fname = raw_input('Enter a file name: ')
if len(fname) == 0:
    fname = 'mbox-short.webarchive'
fhand = open(fname)
for line in fhand :
    line = line.rstrip().upper() # white space remove # upper case
    print line

