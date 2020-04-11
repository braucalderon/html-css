#Exersice 4.38

#Given a list orig,possibly containing duplicate values,show how to use list
#comprehension to produce a new list uniq that has all values from
#the original but with duplicates omitted. Hint: look for indices at
#which the leftmost occurrence of a value occurs.

def value():
    l=eval(input("Enter number: "))
    lis=[]
    for number in l:
        if number not in lis:
            lis.append(number)
            
        
    print (lis)

value()
        
        
        

    
