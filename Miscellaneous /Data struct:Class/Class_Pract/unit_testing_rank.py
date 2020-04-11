
# unit_testing_rank.py
 
from Stack import Stack
import unittest


class StackTest(unittest.TestCase):
    def pushTest(self):
        test = 3                          # create a variable for testing              
        stack = Stack()                   # call the class stack
        stack.push(test)                  # call the method push
        tonto = stack.pop()               # create a new variable calling stack.pop() 
        self.assertEqual(test,tonto)      

    def ziseTest(sel):
        test1 = 34
        stack = Stack() # size of 1
        size = stack.size() # Get the size of the stack
        self.assertEqual(len(test1),size) # compare the size of the stack against the size of the inserted elements

        
        
    
      
    
  

    

unittest.main()

