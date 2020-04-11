

def mode():
    mode=0
    numList = []
    value = input("Next number (hit enter to quit): ")
    numList.append(eval(value))
    value = input ("Next number (hit Enter to quit): ")

    for i in numList:
        i**10
        mode=+i
    print(mode)

mode()
        
        
        
        
