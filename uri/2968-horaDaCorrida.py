from math import ceil

v, n = map(int, raw_input().split())

tmp = v*n
print("%d %d %d %d %d %d %d %d %d" % (ceil(tmp*0.1), ceil(tmp*0.2), ceil(tmp*0.3), ceil(tmp*0.4), ceil(tmp*0.5), ceil(tmp*0.6), ceil(tmp*0.7), ceil(tmp*0.8), ceil(tmp*0.9)))
