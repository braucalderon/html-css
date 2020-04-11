# Example programs

# Given list L, an element x, and an integer k
# returns the position of the kth occurence of x
# If there is no such element, returns -1
def FindK(L,x,k):

    x_count = 0
    L_loc = 0
    L_len = len(L)
    good_pos = -1 # -1 means not found yet
    while L_loc < L_len and good_pos == -1:
        elt = L[L_loc]
        if elt == x and k == x_count:
            good_pos = L_loc
        elif elt == x and k != x_count:
            x_count = x_count + 1

        L_loc = L_loc + 1


    return good_pos

def mode():

    numList = []
    invalue = input("Next number (hit Enter to quit): ")
    while(invalue != ''):
        numList.append(eval(invalue))
        invalue = input("Next number (hit Enter to quit): ")

    mode=0
    highest=0
    count= numList.count
    for i in range (1,101):
        if count(i) > highest:
            mode = i
            highest = count
        return mode
    
    


    
def listToString(L):

    S = ""
    for string in L:
        S = S + string
    return S
    
