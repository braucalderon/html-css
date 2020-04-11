# Implement an algorithm to determine if a string has all unique characters.
from array import *

def checkUniqueness(s):
  """ determines if a string has all unique characters.

     returns True if all characters are unique,
     and False otherwise.
     
     We assume that the string contains only letters of alphabet."""

  s=s.lower()

  print("string: ",s)

  a = array("i",[0]*26) # array of 26 elements, for 26 letters of the alphabet

  #print(a)

  i = 0
  while i < len(s): 

    #print(i,ord(s[i])-97)
    
    if a[ord(s[i])-97]: # if the corresponding letter of alphabet has 1,
      # then it was already met in the word, return False
      return False
    
    else: # if the corresponding letter of the alphabet is 0,
      # then mark that we met it by putting 1
      a[ord(s[i])-97] = 1
      i += 1

  return True

### -----   TESTING -----------

print("Has all unque characters? ",checkUniqueness("abc"))
print("Has all unque characters? ",checkUniqueness("Hello"))
print("Has all unque characters? ",checkUniqueness("equal"))
print("Has all unque characters? ",checkUniqueness("abcdefghijklmnopqrstuvwxyz"))

  
