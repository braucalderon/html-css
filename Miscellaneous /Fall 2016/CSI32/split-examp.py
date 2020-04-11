#split() example
def main():
    string=input("Hello! \n Please enter a list of strings, separated by commas:")

    print(string, type(string))

    l = string.split(',')  # splitting the string into the list of strings,
                           # using ',' as a separation place

    print(l, type(l))

main()    
