# LList.py
from ListNode import ListNode

class LList:

    #------------------------------------------------------------

    def __init__(self, seq=()):

        """create an LList
        post: creates a list containing items in seq"""

        self.last = None
     
        if seq == ():
            # No items to put in, create an empty list
            self.head = None
        else:
            # Create a node for the first item
            self.head = ListNode(seq[0], None)

            # Add remaining items keeping track of last node added
            head = self.head
            for item in seq[1:]:
                head.link = ListNode(item, None)
                head = last.link

        self.size = len(seq)
   
    #------------------------------------------------------------

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    #------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''
        
        assert 0 <= position < self.size


    #-------------------------------------------------------------

    def __max__(self):

        '''post: gets the maximun value'''

        

    #-------------------------------------------------------------

    def __min__(self):

        '''post: gets the minimun value'''

        

    #-------------------------------------------------------------

    def index(self, value):
        
        '''post: returns the length of the string'''
        
        item = value;
        return self.size.index(item)

    #-------------------------------------------------------------

    def count(self, item):

        '''post: returns count of how many objects occurs in list'''
        
        return self.size.count(value)

    #------------------------------------------------------------

    def remove(self):
        pass
    #-------------------------------------------------------------
    def append(self):
        pass
        
    
#-------------------Testing-------------------

    
L = LList([5,1,2,3,4,0,1])
print("Here is our LList:",L)
#print(min(L))
print("The smallest value is ",L.__min__())
print("The largest value is ",L.__max__())
print("index of value 3 is ",L.index(3))
print("index of value 5 is ",L.index(5))
print("index of value 0 is ",L.index(0))
#print("index of value 7 is ",L.index(7))
print("There are",L.count(1),"ones in the list")

print("\n Deleting 3 from the list ... ")
L.remove(3)
print(L)
print("should be: [5,1,2,4,0,1]")

#print("Trying to delete an non-existing value of 10 from the list...")
#L.remove(10)

print("\n The tail node before appending 7:",L.last.item)
print("After appending 7:")
L.append(7)
print(L)
print("The tail's value:",L.last.item)

print("\n Deleting 7 from the list...")
L.pop()
print(L)
print("The tail's value:",L.last.item)

print("\n Appending 12...")
L.append(12)
print(L)
print("The tail's value:",L.last.item)

print("\n Inserting a value 23 at the end...")
L.insert(len(L),23)
print(L)
print("The tail's value:",L.last.item)


        

        

        
        
        

        

    
