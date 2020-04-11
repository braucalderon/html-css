def reverse(text):
    n=len(text) 
    new = ""
    while n:
        n -= 1
        new += text[n]
    return new

print (reverse('fool'))
