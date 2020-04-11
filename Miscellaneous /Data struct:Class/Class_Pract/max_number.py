# max_number.py


def max_number(n):

    if len(n) == 1: # if there is only one number in the list
        return n[0] # return the number in position 0
    else:
        return max(n[0], max_number(n[1:])) # max_number(n[1:]) calls the fuct again
                                            # until the max value is found
                                            # [1:] starts from position 1 


n=[13,2,5,4,8,6,12]
print(max_number(n))


##
##def sumar(n):
##
##    if n == 5:
##        return n
##
##    else:
##        return sumar(n + 1)
##
##
##print(sumar(1))
