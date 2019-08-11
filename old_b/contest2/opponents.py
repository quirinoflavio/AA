n, d = map(int, raw_input().split())


c = 0
m = 0
for i in xrange(d):
    p = list(raw_input())
    s = set(p)
    if len(s) > 1 or s.pop() == '0':
        c += 1
    else:
        if c > m: 
            m = c
        c = 0

if c > m: 
    m = c
print m