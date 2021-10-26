alice = map(int, list(raw_input()))
bob = map(int, list(raw_input()))

n = len(alice)


smallest = alice

def swap(k, l):
    smallest[k], smallest[l] = smallest[l], smallest[k]


for i in xrange(n):
    for j in xrange(i, n):
        if i != 0 and smallest[i] > smallest[j]:
            swap(i, j)
        elif smallest[i] > smallest[j] and smallest[j] != 0:
            swap(i, j)

if smallest == bob: print "OK"
else: print "WRONG_ANSWER"

