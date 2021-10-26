def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
n = int(raw_input())
 
def mmc(a, b):
    return (a*b) / gcd(a, b)
 
ab = []
lista = []
for i in xrange(n):
    a, b = map(int, raw_input().split())
    ab.append((a, b))
    lista.append(mmc(a, b))
 
 
p = lista[0]
w = p
for x in xrange(1, n):
    p = gcd(p, lista[x])
q = p
 
for g in xrange(n):
    l = gcd(p, ab[g][0]) 
    if l != 1:
        p = l
    l = gcd(p, ab[g][1]) 
    if l != 1:
        p = l
    
 
if p == 0:
    print w, q
print int(p) if p!=1 else -1