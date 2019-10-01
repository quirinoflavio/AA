from collections import defaultdict, deque

n, k = map(int, raw_input().split())

c = map(int, raw_input().split())

tela = defaultdict(int)
deq = deque()
cont = 0

for i in xrange(n):
    if cont < k and tela[c[i]] == 0:
        tela[c[i]] = 1
        deq.appendleft(c[i])
        cont += 1
    elif cont == k and tela[c[i]] == 0:
        tela[deq.pop()] = 0
        deq.appendleft(c[i])
        tela[c[i]] = 1

deq.reverse()
print cont
for i in xrange(cont):
    print deq.pop(),


