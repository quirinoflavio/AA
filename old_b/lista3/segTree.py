MAXN = 400000
INF = 1000

segTree = [ 0 for x in xrange(MAXN)]
arr = []

def build(id, l, r):
    if l == r:
        segTree[id] = arr[l]
    else:
        m = (l + r) / 2
        build(id*2, l, m)
        build(id*2+1, m+1, r)
        segTree[id] = min(segTree[id*2], segTree[id*2+1])

def update(id, l, r, v, pos):
    if l == r:
        segTree[id] = v
    else:
        m = (l + r) / 2
        if pos <= m:
            update(id*2, l, m, v, pos)
        else:
            update(id*2+1, m+1, r, v, pos)
        segTree[id] = min(segTree[id*2], segTree[id*2+1])

def query(id, l, r, x, y):
    if x <= l and r <= y:
        return segTree[id]
    elif y < l or r < x:
        return INF
    else:
        m = (l + r) / 2
        return min(query(id * 2, l, m, x, y), query(id*2+1, m+1, r, x, y))
