c = int(raw_input())

cs = [ tuple(map(int, raw_input().split())) for x in xrange(c)]

s = int(raw_input())

for v, row in enumerate(cs):
    if row[0] <= s and s <= row[1]:
        print c-v