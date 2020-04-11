

def mode():

    numList = []
    invalue = input("Next number (hit Enter to quit): ")
    while(invalue != ''):
        numList.append(eval(invalue))
        invalue = input("Next number (hit Enter to quit): ")

    mode=0
    highest=0
    for i in range (1,101):
        count = numList.count(i)
        if count > highest:
            mode = i
            highest = count

    print(mode)
    input("Hit enter to quit.")

mode()
    
    

