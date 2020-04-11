#Finobbaci


def fibonacci(n):


    print('Calculating finobacci of '+ str(n))
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        
        return fibonacci(n-1) + fibonacci(n-2)
    


def main():

    while True:
        try:
            n=eval(input('\nEnter a positive integer to calculate the Finobbaci number: '))
            if n > 0:
                break
            else:
                print('\nInput must be non-negative integers')
                   
        except SyntaxError:
            print('\nNumericals inputs only')

        except NameError:
            print(' \nInput must be an integer')
        

    fb=fibonacci(n)
    print ('\nThe Finobacci of %d = %d'%(n,fb))

main()
