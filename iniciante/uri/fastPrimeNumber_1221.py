import math
c = int(input())
for i in range(c):
    div = 0
    a = int(input())
    if a <= 2:
        if a == 2:print("Prime")
        else: print("Not Prime")
        continue
    for j in range(2,int(math.sqrt(a))+1):
        if a % j == 0: div += 1
        if div == 2: break

    if div >= 1: print("Not Prime")
    else: print("Prime")
