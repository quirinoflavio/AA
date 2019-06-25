k = int(raw_input())
l = int(raw_input())

counter = 0
while (l != k and l >= 2):
    l, ll = l/k, l/(k*1.0)
    if (l != ll): break
    counter += 1

if l==k:
    print "YES"
    print counter
else:
    print "NO"