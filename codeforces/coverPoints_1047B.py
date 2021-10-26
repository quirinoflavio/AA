n = int(raw_input())
maxx = 0

for i in xrange(n):
    x, y = map(int, raw_input().split())
    if x+y > maxx: maxx = x+y

print maxx
