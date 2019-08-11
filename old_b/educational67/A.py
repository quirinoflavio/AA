q = int(raw_input())
for i in xrange(q):
    n, s, t = map(int, raw_input().split())

    if s+t > n:
        com = n - max(s, t)
        both = min(s, t) - com 
        print max(s, t) - both + 1
    else: 
        print n - min(s, t) + 1