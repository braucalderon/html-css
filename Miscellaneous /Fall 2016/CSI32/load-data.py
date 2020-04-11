
def greetings():
    print('This program tries to open a file with the name provided by the user,\n',
          'and read all the data into a two-dimensional array/list',
    'The data must consist of integer numbers, separated by spaces.')

def processData(data):
    rows = len(data) # number of rows is the number of elements in the list
    # number of columns is the number of elements is each string of the list
    # we will get later

    print('number of lines is',rows)
    
    A=list()

    cols=0
    for r in range(rows):
        line=data[r].split() # split by white space, store is a list

        if r == 0: # getting the number of elements in each string of the list
            cols=len(line)
            print('number of elements in each line is ',cols)

        if len(line) != cols:
            print('Warning: line %d:'%(cols+1))

            raise ValueError('number of elements in this line is different from the lines above')

        # use list comprehension to convert each element to integer
        line_int=[int(elem) for elem in line]
            
        # appent the list of integers to list A as a next element of list A
        A.append(line_int)

    return A

def display(A):

    cols=len(A[0])
    for i in range(len(A)):
        for j in range(cols):
            print(A[i][j],end=" ")
        print()

def main():

    greetings()

    while True:

        fname=input('Please, input the name of the data file:')
        
        try:
            f=open(fname)
            break
        except ValueError:
            print('cannot open file',fname)
            

    print('File %s is opened successfully!'%fname)

    
    # read all the data from the given data file
    # store it in a list, the result is a list of strings
    data = f.readlines()

    # form a two-dimensional array
    A=processData(data)

    print(A)

    # display the information
    display(A)

main()    
