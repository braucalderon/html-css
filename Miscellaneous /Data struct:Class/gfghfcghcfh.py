'''
w = [2,4,2,5,8,2,5,4]

d = dict()

for i in w:
    d[i] = d.get(i, 0) + 1


print (d)
'''

import string

s = "#pendejo!@#^&&*@*("

for i in string.punctuation:
    s = s.replace(i, '')

print(s)


    
 
