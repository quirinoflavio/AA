import math
s = set()
def montaP(s):
    p = [1 for x in range(1000001)]
    for i in range(2, 1000000-1):
        if p[i]:
            s.add(i*i)
            for k in range(2*i, 1000001, i):
                p[k] = 0
c = int(input())
q = map(int, raw_input().split())
montaP(s)
for i in range(c):
    if q[i] in s: print("YES")
    else:print("NO")
