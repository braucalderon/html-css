# HW 13

# implement addition of two matrices
# new matrix should be displayed and save in a output file

import time
print('This program will acomplish the sum of two Matrices with the same number \nof rows and columns')   

def matrix(A,B):
    
    r=[]
    for k in range(len(A)):
        tmp=[]
        for i in range(len(A[0])):
            tmp.append(A[k][i]+B[k][i])
        r.append(tmp)    

    #print(r)
    #print()
    return r

def processdata(f_data): # one argument needed to process both files
    # argument must be the object that must be processed 
    rows = len(f_data)
    
    A=list()

    cols=0
    for r in range(rows):
        line=f_data[r].split()

        if r == 0: # getting the number of elements in each string of the list
            cols=len(line)
            print('Number of Columns in the file',cols)

        if len(line) != cols:
            print('Warning: line %d:'%(cols+1))

            raise ValueError('Colums are not equal')

        line_int=[int(elem) for elem in line]
            
        # appent the list of integers to list A as a next element of list A
        A.append(line_int)

    return A


def display(C): #any argument can be added
    
    m='' # empty variable, will store result into it
    cols=len(C[0]) # C same as the argument
    
    for i in range(len(C)):# C must be the same as the argument 
        for j in range(cols):
            m+=(str(C[i][j]))# C must be the same as the argument
            m+=(" ")
                
        m+="\n"
    print()
    return m # without it, result cannot be copy into the new file created

def main():

    while True:
        fname=input('\nPlease input the first file: ')
        fname1=input('Please input the second file: ')

        try:
            f=open(fname)
            f1=open(fname1)
            break
        
        except ValueError:
            print ('\nOne of the files cannot be opened')

        except FileNotFoundError:
            print ('\nOne of the files could not be found' )
        
    f_data= f.readlines()
    f1_data= f1.readlines()
    
    
    # def processdata() only needs one argument(f_data) to process both files
    A=processdata(f_data)
    B=processdata(f1_data)


    # must create variable to call function into def main()
    t=matrix(A,B)
    
    print('\nThe sum of the two Matrices uploaded is:')
    print(display(t)) #print result from r=matrix(A,B) in shell 


    # from this point on, file will be created
    while True:
        file=input('To save the result in a file enter < y >, otherwise < n >: ')

        if file != 'y':
            print('No file was created')
            time.sleep(1)
            quit()
            
        if file == 'y':
            fname2=input('Please enter a file name: ')
            
            try:
                f2=open(fname2, 'w')
                break
            
            except ValueError:
                print('The file could not be created')

    # variables to print into the new file created            
    a=(display(t))
    b=('-------------')
    c=(display(A))
    d=(display(B))
    e=('  +  ')
    f=('Result:')

    # prints to the file created, from variables a,b,c,d,e,f
    # file=f2 will print the variables created into the new file
    print(c,file=f2), print(e,'\n',file=f2), print(d,file=f2)
    print(b,file=f2)
    print(f,'\n',file=f2)
    print(a,file=f2)

    #prints to the shell in python 
    print('File has been saved')
                 
    
    
main()
