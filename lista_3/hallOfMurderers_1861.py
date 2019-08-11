dicM = {}
mM = {}
while True:
    try:
        m, k = input().split()
        if m in dicM:
            dicM[m] += 1
        else:
            dicM[m] = 1
        mM[k] = 0
    except EOFError:
        break
print("HALL OF MURDERERS")
lista = []
for mu in dicM:
    if mu not in mM:
        lista.append(mu)
saida = sorted(list(lista))
for i in saida:
    print(i, dicM[i])
