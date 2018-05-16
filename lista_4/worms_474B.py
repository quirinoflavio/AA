from sys import stdin, stdout

qp = int(stdin.readline())
pilhas = list(map(int, stdin.readline().split()))

qw = int(stdin.readline())
w = list(map(int, stdin.readline().split()))

d = {i:w[i] for i in range(qw)}

w.sort()

qa = 0
pa = 0
saida = []
for i in range(qw):
    while pa < qp:
        qa += pilhas[pa]
        if w[i] <= qa:
            saida.append(pa)
            pa += 1
            break
        
        pa += 1
#printar elementos na ordem.
print(d)
for i in saida:
    print(i)
    #print(d[i])
