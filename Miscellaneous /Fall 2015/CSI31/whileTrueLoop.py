while True:
    x = eval (input("Enter a positive number: "))
    if x >= 0:
        break # Exit loop if number is valid
    else:
        print ("The number you entered was not valid")
print ("Valid number: ", x)
