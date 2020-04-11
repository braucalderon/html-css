def prime():
    p=True
    for k in range(2,n):
        ifi n % k == 0:
            p=False
    return p

# prime(1+2) / checks (n+2)%2==0 not true = not prime
def counttwinprime(n):
    count=0
    for i in range (2,n):
        if prime(i) and prime(1+2):
            count=count +1
    return count 
