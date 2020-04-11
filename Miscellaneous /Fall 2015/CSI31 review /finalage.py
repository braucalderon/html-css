def age():

    s=eval(input("Please enter your age: "))
    while s < 0:
        s=eval(input("Please enter your age: "))
    if s < 18 and s < 65 and s > 0:
        print ('Your are a minor')
    if s > 18 and s < 65:
        print ("You're a worker")
    else:
        print("You're retired")
               
           
age()
