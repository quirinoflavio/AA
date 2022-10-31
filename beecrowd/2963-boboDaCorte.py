n = int(raw_input())
l = []

for i in xrange(n):
    l.append(int(raw_input()))

if(max(l) == l[0]):
    print("S")
else:
    print("N")