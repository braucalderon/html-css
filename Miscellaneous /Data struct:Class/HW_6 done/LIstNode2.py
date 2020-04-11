# ListNode2.py




class ListNode2:

    def __init__(self, item = None, leftL = None, rightL = None):

        '''creates a ListNode with the specified data value and
           two links: to the previous node and to the next node
        post: creates a ListNode with the specified data value and links'''

        self.item = item
        self.leftL = leftL
        self.rightL = rightL
    

    def __str__(self):
      ''' for printing the node '''
  
      return str(self.item)

class Doublelink:

    def __init__(self, tail = None, head = None):

        #ListNode2.__init__(self)
        self.tail = tail
        self.head = head

    def append(self, x):

        newNode = ListNode2(x) # call the ListtNode2
        if self.head is not None:   # if the object is not absence of a value
            self.head = newNode
            self.tail = newNode   # it makes a new node 

        else:
            newNode.leftL = self.tail # bl bla
            newNode.rightL = newNode  # blaba
            #self.tail.leftL = newNode
            self.tail = newNode

    def insert(self, i, x):
        
        newNode = ListNode2(x)
        if self.head == None:
            self.head = newNode

        else:
            newNode.leftL = self.head
            newNode.leftL.rightL = newNode
            self.head = newNode
            
##        if i == 0:
##            self.head = newNode(x, self.head)
##
##        else:
##            newNode.leftL = None
##            newNode.leftL = newNode(x,newNode.leftL)
        
            

    def remove(self, term):
        pass


##
##        new = self.head
##
##        while new is not None:                      # if self.head is noy an empty value
##            if term == new.term:                 
##                if new.leftL is not None:                 # if self.head has not an empty value
##                    new.leftL.rightL = new.rightL   # it moves the object to the right
##                    new.rightL.leftL = new.leftL
##
##                else:
##                    new = new.rightL
##                    new.rightL.leftL = None
##                    
##            new = new.rightL
            

def printLR(headNode):
    """ prints all elements following right links, starting with the headNode """
    node = headNode
    #listV = []
    while headNode is not None:
##        listV.append(headNode.item)
##        print(headNode.item)
        print(headNode.item, end = "\t")
        headNode = headNode.rightL

    print("end of linked list")
    #print(listV)

def printRL(tailNode):
    """ generates a list all elements following left links,
    starting with the tailNode """
    
    node = tailNode
    listV = []
    
    while node is not None:
        listV.append(node.item)
        node = node.leftL

    print(listV)
    listV = listV[::-1]
    print("here is the list of elements, following left links:",listV)

    return listV

    
def main():


    D = Doublelink()
    
    D.append(35)
    D.append(1)
    D.append(23)
    D.append(7)
    D.append(10)
     

    printLR(D.head)
    printRL(D.tail)

    D.insert(8,1)
    printLR(D.head)
    
    D.remove(7)
    printLR(D.head)
    printRL(D.tail)

    # Issue: I don't know how to print it correctly 

 
    

 
main()
