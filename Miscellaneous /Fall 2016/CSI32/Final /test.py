def tsf(n):
    if n//2!=0:
        m=tsf(n//2)
        return m + str(n%2)
    else:
        return str(n%2)

def main():
    p=2
    print(tsf(p))
main()
