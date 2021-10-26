from math import ceil

n = int(raw_input())

for i in xrange(n):
    p = int(raw_input())
    g = map(int, raw_input().split())
    print int(ceil(sum(g)/(p*1.0)))