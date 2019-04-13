from time import time
from sys import stdin, stdout
segTree = [ 0 for x in xrange(3000000)]

cf = 0
query_time = 0
def getNode(b):
    return (1,0,0) if b=='(' else (0,0,1)

def crossOver((a1, b1, c1), (a2, b2, c2)):
    inicio = time()
    b = b1 + b2 + min(a1, c2)
    oa1 = min(a1, c2)
    a1 -= oa1
    c2 -= oa1

    a = a1 + a2
    c = c1 + c2
    
    cf += time() - inicio
    return (a, b, c)

def build(id, l, r):
    inicio = time()
    if l == r:
        segTree[id] = getNode(arr[l-1])
    else:
        m = (l + r) / 2
        build(id*2, l, m)
        build(id*2+1, m+1, r)
        segTree[id] = crossOver(segTree[id*2], segTree[id*2+1])
    #print "build: " + str(time() - inicio)

def query(id, l, r, x, y):
    inicio = time()
    if x <= l and r <= y:
        return segTree[id]
    elif y < l or r < x:
        return (0,0,0)
    else:
        m = (l + r) / 2
        return crossOver(query(id * 2, l, m, x, y), query(id*2+1, m+1, r, x, y))
    query_time += time() - inicio


arr = stdin.readline().strip()
#arr = ')' * 1000000
n = len(arr)
#q = int(raw_input())
q = 100000
inicio = time()
saida = ""
build(1,1,n)
for i in xrange(q):
    q1, q2 = map(int, stdin.readline().split())
    saida += str(query(1,1,n,q1,q2)[1]*2)

print "query:" + str(query_time)  
print "crossover:" + str(cf)
print saida
fim = time()
print fim-inicio