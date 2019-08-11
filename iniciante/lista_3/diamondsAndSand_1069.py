from collections import deque
ct = int(input())

for i in range(ct):
    diamantes = 0
    d = deque()
    ent = input()
    for c in ent:
        if c == "<":
            d.append("<")
        if c == ">":
            if len(d) != 0:
                d.pop()
                diamantes += 1
    print(diamantes)
