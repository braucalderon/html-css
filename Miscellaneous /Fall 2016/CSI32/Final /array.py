from copy import deepcopy

class Array:
  """ Array is a sorted collection of integer values """
  
  def __init__(self,sequence = []):
    self._array = deepcopy(sequence)  # copying all elements from sequence into se;f._array
    self._array.sort() # calling the built-in sort method

  def __str__(self): # overriding the display method for class Array
    x = ""
    for item in self._array:
      x += str(item) + ", "
    return x[:len(x)-2]

  def __min__(self,f):
    """ returns smallest value in the array """
    return a3

  def __max__(self):
    """ returns largest value in the array """
    pass
    
  def __add__(self, other):
    """ if two arrays are added then a new array is created and it contains all the elements of both arrays
        (repetitions of values are allowed);
        if an array and an integer value are added, then a new array is created and it contains all the
        elements of the array and the integer value (repetitions are allowed) """
    pass

  def __sub__(self, other):
    """ other is either another array or an integer to be removed;
    removes all the elements of second array from the first array,
     or removes an integer value from the array;
     generates a new array"""

    tmp = deepcopy(self._array)

    if isinstance(other,Array): # if other is another array
      for value in other._array:
        try:
          tmp.remove(value)
        except:
          pass
          
    elif isinstance(other,int):# if other is an integer value
      try:
        tmp.remove(other)
      except:
        pass

    else: # all other cases
      pass

    return Array(tmp)
        
  def average(self):
    """ returns the average of the array values """
    pass

  

def main():
  a = Array([1,5,3,4,2])
  print("The array A:",a)

  b = a - 1

  print(a," - ",1," = ", b)

  c = Array([5,7])

  b2 = a - c

  print(a," - ",c," = ", b2)

  a2 = a+7

  print(a, " + ", 7, " = ",a2)
  
  d = Array([10,12,4,13,1])
  a3 = a + d
  print(a, " + ", d, " = ",a3)


  print("smallest value of", a3," is ", a3.min())

  print("largest value of", a3," is ", a3.max())

  print("median value of",a3," is ", a3.median())
  
  print("median value of",a," is ", a3.median())

main()  
      
  
