
class List_Node():

    def __init__(self,item = None, link = None, left = None, right = None ):

        self.link = link
        self.item = item
        self.right = right
        self.left = left 
        
        


    def __str__(self):

        return str(self.item)
    

def print_list(node):
    
  if node == None: # it means that there are no more nodes in the list
    print("No more elements in the list")
  else: # more elements are available
    print(node.item,"\t",end="")
    print_list(node.link)


def main():

    n = List_Node(5)
    n1 = List_Node(3,n)
    n2 = List_Node(7,n1)
    n3 = List_Node(25, n2)

    print_list(n3)

    

    n05 = List_Node(30,n1.link)
    n1.link = n05

    print_list(n3)

    

    
 

main()
    

        
