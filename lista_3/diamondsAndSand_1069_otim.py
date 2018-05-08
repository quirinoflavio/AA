for i in range(int(input())):
    a, b = 0, 0
    for c in input():
        if c == "<":
            a += 1
        elif c == ">" and a > 0:
            a -= 1
            b += 1
    print(b)
