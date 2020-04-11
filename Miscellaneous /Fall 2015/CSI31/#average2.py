def main():
    sum=0.0
    count=0
    moredata="yes"
    while moredata[0] == "y":
        x=eval(input("Enter a number >> "))
        sum=sum+x
        count=count+1
        moredata=input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", sum/count)
    
main()
                       
#Notice this program uses string indexing (moredata[0])
#to look just at the first letter of the user’s input.
#This allows for varied responses such as “yes,” “y,” “yeah,” etc.
#All that matters is that the first letter is a “y.”
