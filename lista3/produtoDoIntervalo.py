from sys import stdin, stdout

MAXN = 400000

segTree = [ 0 for x in xrange(MAXN)]

def value(x):
    return 1 if (x > 0) else (-1 if (x < 0) else 0)

def build(id, l, r):
    if l == r:
        segTree[id] = value(arr[l-1])
    else:
        m = (l + r) / 2
        build(id*2, l, m)
        build(id*2+1, m+1, r)
        segTree[id] = segTree[id*2] * segTree[id*2+1]

def update(id, l, r, v, pos):
    if l == r:
        segTree[id] = v
    else:
        m = (l + r) / 2
        if pos <= m:
            update(id*2, l, m, v, pos)
        else:
            update(id*2+1, m+1, r, v, pos)
        segTree[id] = segTree[id*2] *  segTree[id*2+1]

def query(id, l, r, x, y):
    if x <= l and r <= y:
        return segTree[id]
    elif y < l or r < x:
        return 1
    else:
        m = (l + r) / 2
        return query(id * 2, l, m, x, y) * query(id*2+1, m+1, r, x, y)

def getSaida(x):
    return "+" if x > 0 else ("-" if x < 0 else "0")


testes = stdin.readlines()
while True:
    try:
        N, K = map(int, raw_input().split())
        arr = map(int, raw_input().split())
        saida = ""
        build(1, 1, N)
        for i in xrange(K):
            op, i, x = raw_input().split()
            i, x = int(i), int(x)
            if op == "P":
               saida += getSaida(query(1, 1, N, i, x))
            else:
                update(1, 1, N, value(x), i)
        print saida
    except EOFError:
        break






