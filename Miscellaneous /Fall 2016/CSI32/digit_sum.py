#important exercise

def digit_sum(n):
    lis=[] #make an empty list
    total=0
    for number in str(n): #turn into string
        number = int(number)#then back into number 
        lis.append(number)# add all of them to the empty list
        total = sum(lis)# sum up all number in list 
    print (total) # return the sum 
    
digit_sum(1234) 
