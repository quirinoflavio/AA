def c_m(a, e):
    cont = 0
    for i in a:
        if i > e:
            cont += 1
    return cont

ct = int(input())

for i in range(ct):
    qntd = int(input())
    h = list(map(int, input().split()))
    pos = list(map(int, input().split()))

    lista = [[] for x in range(qntd)]

    for p in range(qntd):
        lista[pos[p]].append(h[p])

    lord = []
    i = 0
    while len(lord) < qntd:
        if i < len(lista) and len(lista[i]) == 0:
            i += 1
        elif i <= len(lord) and c_m(lord, min(lista[i])) == i:
            lord.append(min(lista[i]))
            lista[i].remove(lord[-1])
            i += 1
        else:
            i = 0

for i in range(0, len(lord)-1):
    print(lord[i], end=" ")
print(lord[-1])
