def sub(n):
    if(n == 0):
        return 3
    return n-1

n = int(raw_input())

while(n != 0):
    s = raw_input()
    p = 0

    for i in xrange(n):
        if(s[i] == "D"):
            p = (p+1) % 4
        else:
            p = sub(p)

    if(p == 0):
        print("N")
    elif(p == 1):
        print("L")
    elif(p == 2):
        print("S")
    else:
        print("O")

    n = int(raw_input())