while (True):
    entrada = list(map(int, input().split()))

    if entrada == [0,0,0,0]:
        break

    if entrada[0] == 0:
        entrada[0] = 24
    if entrada[2] == 0:
        entrada[2] = 24

    t1 = (entrada[0] * 60) + entrada[1]
    t2 = (entrada[2] * 60) + entrada[3]

    if t1 > t2:
        print(1440 + t2 - t1)
    else:
        print(t2-t1)
