# this file contains definition of the Set class

class Set:

    counter = 0 # class-level attribute
    
    def __init__(self, l):
        ''' constructor of class Set '''
        n=len(l)
        # generating list with unique elements (see List Comprehension lecture)
        self._contents=[l[i] for i in range(n) if l[i] not in l[i+1:n]]

        Set.counter += 1 # class variable
        # every time an instance of class Set is created, the counter is incremented by 1

    def __str__(self):
        ''' print method '''
        return str(self._contents)

    def __contains__(self,value):
        ''' checks presence of element in the Set object '''
        return value in self._contents

    def add(self,value):
        ''' adds element to the Set object '''
        if value not in self._contents:
            self._contents.append(value)

    def discard(self,value):
        ''' discards an element from the Set'''

        ''' If the value is an element of the Set object, it removes it, otherwise does nothing.'''
        if value in self._contents:
            self._contents.remove(value)

### --------------   TESTING ------------------------            

def main():
    lst = input("Please, input a list of elements, separated by commas:")

    l = lst.split(',')
    s = Set(l)

    print("Here is our set s: ", s)

    print("\n Trying to add \'mother\' to the set s: ")
    s.add('mother')
    print(s)

    lst2 = input("Please, input another list of elements, separated by commas:")

    l2 = lst2.split(',')
    s2 = Set(l2)

    print(s2)
    print(s.counter, s2.counter)

    print("\n Trying to remove \'my\' from the set s:")
    s.discard('my')
    print(s)

    if 'mother' in s:
        print("\n \'mother\' is in the set s")

main()    
        
