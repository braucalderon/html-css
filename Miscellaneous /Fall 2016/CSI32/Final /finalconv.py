def conv(n):
    m = n//8
    if m != 0:
        return conv(m) + str(n%8)
    else:
        return str(n%8)

def main():
    n=1
    t=conv(n)
    print(t)

main()
