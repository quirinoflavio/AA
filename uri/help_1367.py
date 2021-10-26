from collections import defaultdict as dd
while True:
    n = int(raw_input())
    if n == 0: break

    inc = dd(int)
    cor = dd(int)
    total = 0
    c = 0
    for i in xrange(n):
        
        p, t, j = raw_input().split()
        t = int(t)

        if j == "incorrect": inc[p]+=20
        elif j == "correct": total, c = total + inc[p] + t, c + 1
    print c, total