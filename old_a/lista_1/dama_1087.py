while(True):

    x1, y1, x2, y2 = map(int, input().split())

    if x1 == 0:
        break

    if x1 == x2 and y1 == y2:
        print("0")
        continue

    elif x2 == x1 or y2 == y1:
        print("1")
        continue

    saida = "2"
    for i in range(1, 9):

        if x1+i==x2 and y1+i==y2 or x1-i==x2 and y1-i==y2:
            saida = "1"
            break

        elif x1+i==x2 and y1-i==y2 or x1-i==x2 and y1+i==y2:
            saida = "1"
            break

    print(saida)
