while True:
    try:
        n = int(raw_input())
        l = map(int, raw_input().split())

        m = sum(l)/float(n)

        if(m % 1 != 0):
            print("-1")
        else:
            res = 1
            for i in xrange(n):
                res += max(int(m) - l[i], 0)

            print(res)
    except EOFError:
        break