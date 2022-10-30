s = raw_input()
l = [1, 2, 6, 24, 120]

while(s != "0"):
    res = 0

    k = 0
    for i in xrange(len(s)-1, -1, -1):
        res += int(s[i])*l[k]
        k += 1

    print(res)

    s = raw_input()