
def getData():
    ''' reads the infromation from a file and stores it in a list,
    where every element is a tuple of integer values '''
    
    while True:
        filename=input('Please, input the filename:')
        try:
            input_source=open(filename)
            break
        except IOError:
            print('Cannot open the file. Try again, please')

    listLines=input_source.readlines()
    print('read from file:', listLines)

    input_source.close()
    print('File is closed')

    n=len(listLines)
    data=[]
    
    for i in range(n):
        pair=listLines[i].split()
        print(pair)
        data.append((int(pair[0]),int(pair[1])))

    print(data)
    return data

def display(data):
    ''' displays the information as 2 columns table '''

    n=len(data) # getting number of tuples
  
    #displaying the top of the table
    print(format('x ','4s'),format('y ','4s'),sep='|',end='|\n')
    #print("%4s|%4s"%("x ","y ")) - Python 2 formatting
    print("----|"*2)
    
    # displaying the data
    for i in range(n):
        print(format(data[i][0],'4d'),format(data[i][1],'4d'),sep='|',end='|\n')
        #print("%4d|%4d"%tuple(data[i])) - good for Python 2
    print("----|"*2)

def findSums(data):
    ''' finds sum of values in the first column and in the second column,
        separately.

        data should be a list of tuples '''
    
    n=len(data)

    sumx, sumy = 0,0
    
    for i in range(n):
        sumx += data[i][0]
        sumy += data[i][1]

    return [sumx,sumy]

def main():

    # get data from the input file
    data=getData()

    # display data
    display(data)
    
    # find sum
    result=findSums(data)

    # display the result
    print(format(result[0],'4d'),format(result[1],'4d'),sep='|',end='|\n')
    #print('%4d|%4d'%tuple(result)) - good for Python 2

    
main()


    
