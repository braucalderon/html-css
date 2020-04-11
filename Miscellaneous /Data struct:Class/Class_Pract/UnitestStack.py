# UnitTesting Stack.py's push and size methods

from Stack import *
import unittest

class Tests(unittest.TestCase):
   
  def testPush(self):
    """ tests push method by putting a value into a stack, and retrieving it"""
    testvalue = 23
    mystack = Stack()
    mystack.push(testvalue)

    self.assertEqual(mystack.pop(),testvalue)

  def testSize(self):
    """ test the size method by putting values from the sequence into a stack,
    and verifying the size of the stack with the length of the sequence """
    teststackseq = [11,22,33,44,55,66,77,88,99] # length is 9
    mystack = Stack()
    
    for i in range(len(teststackseq)):
      mystack.push(teststackseq[i])

    self.assertEqual(mystack.size(),len(teststackseq))

unittest.main()
