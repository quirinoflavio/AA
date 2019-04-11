from sys import stdin, stdout
MAXN = 400000

segTree = [ 0 for x in xrange(MAXN)]

def build(id, l, r):
    if l == r:
        segTree[id] = arr[l-1]
    else:
        m = (l + r) / 2
        build(id*2, l, m)
        build(id*2+1, m+1, r)
        segTree[id] = segTree[id*2] + segTree[id*2+1]

def update(id, l, r, v, pos):
    if l == r:
        segTree[id] = v
    else:
        m = (l + r) / 2
        if pos <= m:
            update(id*2, l, m, v, pos)
        else:
            update(id*2+1, m+1, r, v, pos)
        segTree[id] = segTree[id*2] + segTree[id*2+1]

def query(id, l, r, x, y):
    if x <= l and r <= y:
        return segTree[id]
    elif y < l or r < x:
        return 0
    else:
        m = (l + r) / 2
        return query(id * 2, l, m, x, y) + query(id*2+1, m+1, r, x, y)


entrada = stdin.readlines()
saida = ""
N = int(entrada[0])
arr = map(int, entrada[1].strip().split())
build(1,1,N)
i = 2
while (i < len(entrada)):
    op, index = entrada[i].split()
    index = int(index)
    if op == '?':
        stdout.write(str(query(1,1,N,1,index)) + '\n')
    else:
        update(1,1,N,0,index)
    i += 1
