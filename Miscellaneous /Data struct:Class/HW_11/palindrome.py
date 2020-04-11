# palindrome.py

def palindrome(n):

     
    if len(n) < 1:
        return True 
    
    if n[0] == n[-1]: # check string if first and last position are the same
        return palindrome(n[1:-1]) # check and return if reverse first and last
                                   # position string are the same 
    
  
    l = [] # new vairable without special characters 
    for i in n: 
        l.append(i)
        if "," in l:
            l.remove(",")
        if " " in l:
            l.remove(" ")
        if "?" in l:
            l.remove("?")
        if ":" in l:
            l.remove(":")
        if ";" in l:
            l.remove(";")
        if "!" in l:
            l.remove("!")
        if "(" in l:
            l.remove("(")
        if ")" in l:
            l.remove(")")
        if "-" in l:
            l.remove("-")
        if "&" in l:
            l.remove("&")
        if "." in l:
            l.remove(".")
        if "@" in l:
            l.remove("@")
        if "'" in l:
            l.remove("'")
        if "_" in l:
            l.remove("_")
    # print(l) 
    if l[0] == l[-1]:# compare variable if first position and last posistion are the same  
        return palindrome(l[0::-1]) # compare and returns reverse string if first and last
                                    # positions are the same  
    else:
        return False
                   
     
while True:

    n = str(input("Please Input a Phrase:")).lower()

    n_c = n.capitalize()
    
    if palindrome(n) == True:
        print("\nThe string '{}' is a Palindrome".format(n_c))

    else:
        print("\nThe String '{}' is not a Palindrome".format(n_c))

    r = input("\nPress F to quit, else any other key: ").lower()

    if r == "f":
        break
    
    


