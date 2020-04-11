def main():
    sum=0.0
    count=0
    xstr=input("Enter a number and (<Enter> to quit) >> ")
    while xstr != "":
        x=eval(xstr)
        sum=sum + x
        count+= 1
        xstr=input("Enter a number (<Enter> to quit) >> ")
    print("\nThe average of the numbers is", sum/count)
main()
