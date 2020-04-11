# Given a phrase that contains letters of the alphabet and spaces only
# rearrange it so that all letters are alphabetically ordered,
# and the spaces are in the original places.
#
#  NOTE: something is not working. Find what


def reArrange(s):
  """ s is of type string, contains only letters of alphabet and spaces
  returns a new string"""

  ls = s.split() # split the string by spaces, get list of words
  #print("ls:",ls)

  lengths = [len(word) for word in ls] # get lengths of all words
  #print("lengths: ",lengths)

  s = sorted(s) # sort the string, spaces will be first, followed by letters
  #print("sorted: ",s)

  result = ""

  number_of_spaces = len(lengths)-1 # to skip the spaces that string s starts with
  #print("number of spaces: ",number_of_spaces)

  index = number_of_spaces
  for k in range(len(lengths)): # iterating over the number of words
    #print("k=",k)
    for i in range(lengths[k]): # iterating over the number of letters in the corresponding word
      #print("i=",i)
      #print("index = ",index)
      result += s[index] # skipping the first spaces,
      index += 1
      # grabbing the next letter
    result += " " # adding the space

  return result

### -----------   TESTING --------------

s1 = "Hello Mark"
print("The rearranged phrase \' ",s1," \' is : ",reArrange(s1))
print("we were expecting \'aeHkl lMor\'")
  
  
