l1 = map(int, raw_input().split())
l2 = map(int, raw_input().split())
res = 0

for i in xrange(3):
    res += max(l2[i] - l1[i], 0)

print(res)