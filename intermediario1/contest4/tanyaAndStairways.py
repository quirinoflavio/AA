n = int(raw_input())
stairs = map(int, raw_input().split())

stair_q = []

counter = 0
for i in xrange(n-1, -1, -1):
    if stairs[i] != 1: counter += 1
    else:
        stair_q.append(counter + 1)
        counter = 0

print len(stair_q)

for s in xrange(len(stair_q)-1, -1, -1):
    print stair_q[s],