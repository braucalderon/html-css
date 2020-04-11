# queInOrder.py

from Queue import Queue



def queueInOrder(someQueue):
    '''
    Import a list from the Queue to verify if the list is sorted in order

    pre: compare a list from Queue, returning a boolean 
    pos: returns the list intact to the Queue 

    '''
#    T = True
    first_elem = int() # variable to be compared
    
    q3=[]        
    for number in range(someQueue.size()):
        second_elem = someQueue.dequeue() # calls the elements from  class Queue:
        q3.append(second_elem)
        
#        print(second_elem)
         
#        if second_elem < first_elem: # compares the elements, if first is 
#            print(second_elem)          # greater than the second one
#            T =  False
            
             

#        first_elem = second_elem # copy the elemnts into first_elem
#        print(first_elem)
#        someQueue.enqueue(second_elem) # export the elemtns back into the Queue     
            
    return sorted(q3)    # return True if elements are in order
       

def main():



    someQueue = Queue()

    someQueue.enqueue(1)
    someQueue.enqueue(2)
    someQueue.enqueue(10)
    someQueue.enqueue(5)
    someQueue.enqueue(6)
    someQueue.enqueue(7)

    print(queueInOrder(someQueue))

    for numbers in range(someQueue.size()):
        print(someQueue.dequeue())

    if queueInOrder(someQueue) == True:
        print("The Queue in question is in Order!")

    else:
        print("The Queue in question is not in Order!")
    

main()
    

    

    
    

 

