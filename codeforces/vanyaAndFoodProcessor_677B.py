n, h, k = map(int, raw_input().split())

potatos = map(int, raw_input().split())

soma = 0
res = 0

for i in xrange(n):
    soma += potatos[i]
    if soma > h:
        soma = potatos[i]
        res += 1
    res += soma/k
    soma = soma%k
    
if soma > 0: res += 1
print res