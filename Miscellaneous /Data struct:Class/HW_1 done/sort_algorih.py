# Page 37 Exercise 3

from time import time 

def SelectionSort(n):
   
   """Sorted a list of elements in increasing order using Selection Sort

    pre-condition: compare elements from min to the biggest element.
    post-condition: return the sorted list of product n  in incressing order. """

    
   loc=[]
   for i in range(0,len(n)):
      #print(i)
      for j in range(i+1,len(n)):
         #print (j)
         if n[j] < n[i]:             # find the min element 
             loc = n[j];             # store the min element 
             n[j] = n[i];            # re-assign the min element  
             n[i] = loc;

   return n                         # returns the new sorted elements


start = time()
n=[4,46,78,45,5,2,1,67]
print(SelectionSort(n))
end = time()
print ("Running time: ", end - start)







##n_list=(input("\nEnter the elements: "))
###n=list(map(int, eval(n).split()))
##n=theta_n(n)

              





"""
_________________________ _____________________________


Running time

0-notation
T(n) = 5n^2 + 3

Theta notation
T(n) = n^2

__________________________  _____________________________

"""
