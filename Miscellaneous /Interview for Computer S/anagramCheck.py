# this program that checks whether the given two strings are anagrams or not

def anagramCheck(str1,str2):
  """ str1 and str2 are of type string
      checks whether str1 and str2 are anagrams """

  print("\nThe original strings:")
  print(str1)
  print(str2)

  str1 = str1.lower() # converting to lower case
  str2 = str2.lower() # converting to lower case

  s1 = sorted(str1) # sort alphabetically, returns list of characters
  s2 = sorted(str2) # sort alphabetically, returns list of characters
  # comment: all punctuation symbols will be in the beginning of the list,
  # followed by sorted letters
  

  i = 0 # index for str1
# find the first occurence of a letter from the alphabet
  while ord(s1[i]) < 97 or ord(s1[i]) > 122: 
    i += 1

  j = 0
  # find the first occurence of a letter from the alphabet
  while ord(s2[j]) < 97 or ord(s2[j]) > 122:
    j += 1

    
  if len(s1) - i != len(s2) - j:  # quick check O(1) for thier lengths, they should be the same
    return False

  else:
    while i < len(s1) and j < len(s2):
      if s1[i] == s2[j]:
        i+=1
        j+=1
      else:
        return False

    return True
    
### ------------   TESTING -----------------

print("Anagrams? ",anagramCheck("cinema","ice man"))
print("Anagrams? ",anagramCheck("cinema","ice"))
print("Anagrams? ",anagramCheck("William Shakespeare","I am a weakish speller"))
