a, c = map(int, input().split())
while a!=0 and c!=0:

    lista = list(map(int, input().split()))

    laser = a - lista[0]
    for i in range(1, c):
        if lista[i] < lista[i-1]:
            laser += lista[i-1] - lista[i]

    print(laser)
    a, c = map(int, input().split())

