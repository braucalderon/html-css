#Ch 5, question 10

def main():
    fname=input("Please enter a sentence: ")
    words=fname.split()
    t=len(words)
    sum=0 # need to be defined for a loop "below", it does not work if "sum" is
    #not defined
    for word in words:
        w=len(word)
        sum=sum+w # takes the sum of each word (+w) in the sentence and add them all
        # together in the above defined 'sum'. in this case the total is added
        #into sum=0
        average=float(sum)
    print ("The average word lengh of the sentence is: ", average/t)

main()
        
  
        
    
    


