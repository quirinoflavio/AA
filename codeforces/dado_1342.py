segue = True
while (segue):

    num_jog, tam = map(int, input().split())

    if num_jog == 0:
        break

    j = [0, False, 0] * num_jog

    c_j = 0
    for i in range(0, len(j), 3):
        c_j += 1
        j[i] = c_j

    traps = list(map(int, input().split()))

    qntd = int(input())

    continua = True
    while (continua):
        for i in range(2, len(j), 3):
            if j[i-1] == False:
                d1, d2 = map(int, input().split())
                j[i] += d1+d2
                if j[i] > tam:
                    print(j[i-2])
                    continua = False
                    break
            else:
                j[i-1] = False
                continue

            if j[i] in traps:
                j[i-1] = True
