# midterm

def myIterativeFunction(n):

    if n is 0:
        return None
    else:
        print ("*" * n)
        return myIterativeFunction(n-1)
    


def exam(n):
    for i in range(1,n+1):
        print("*" * i)
        
def main():
    
    n= int(input("Enter a number: "))

    print(myIterativeFunction(n))
    print(exam(n))

main()

