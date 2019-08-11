from collections import defaultdict as dd

v, a = map(int, raw_input().split())

dic = dd(list)

for i in xrange(a):
    v1, v2 = map(int, raw_input().split())
    dic[v1].append(v2)
    dic[v2].append(v1)
    

