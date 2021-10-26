from collections import defaultdict
from decimal import Decimal as d

n = int(raw_input())

a = map(int, raw_input().split())
b = map(int, raw_input().split())



dicionario = defaultdict(int)
dicionario['777'] = 0
zeros = 0

for i in range(n):
    if not a[i] and not b[i]:
        zeros += 1
    if a[i] != 0:
        if abs(b[i]) >= 100000000 and abs(a[i]) >= 100000000 and abs(abs(a[i]) - abs(b[i])) < 10:
            variavel = d(b[i]) / d(a[i])
        else:
            variavel = (b[i] + 0.0) / a[i]
        dicionario[variavel] += 1


print max(dicionario.values()) + zeros
