# unittestBST.py

import sys
import unittest
from BST import BST

    
class headache(unittest.TestCase):
 

    def test_insert_rec(self):

        t1 = BST()
        t1.insert_rec(7)
        t1.insert_rec(3)
        t1.insert_rec(8)
        t1.insert_rec(2)
        t1.insert_rec(5)
        t1.insert_rec(9)
        
        values=[2,3,5,7,8,9]
        
        self.assertEqual(t1.asList(),values)


    def test_find_(self):

        t1 = BST()
        t1.insert_rec(7)
        t1.insert_rec(3)
        t1.insert_rec(8)
        t1.insert_rec(2)
        t1.insert_rec(5)
        t1.insert_rec(9)


        value_find=[8,2,9,5]
        value = [11,1,4]

        for i in value_find:
            self.assertEqual(t1.find(i), i)

        for k in value:
            self.assertEqual(t1.find(k), None)

        
        


def main():
    unittest.main()
if __name__ == '__main__':
    main()

