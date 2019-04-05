MAXN = 100000

BiT[0 for x in xrange(MAXN)]

def update(id, v):
    for i in xrange(id, MAXN+1, (i & -i )):
        BiT[i] += v
    
def query(id):
    ret = 0
    for i in xrange(id, 0, -(i & -i)):
        ret += BiT(i)
    return ret

