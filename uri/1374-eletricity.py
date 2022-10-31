#other
from datetime import date

n = int(input())


cont = True
while (cont):
    count = 0
    days = 0
    if n == 0: 
        cont = False
        break
    if n != 0:
        d1, m1, y1, c1 = list(map(int, input().split()))
        d1 = date(y1,m1,d1)
        n -= 1

    while(n != 0):
        d2, m2, y2, c2 = list(map(int, input().split()))
        d2 = date(y2,m2,d2)
        ans = d2-d1
        cost = c2 - c1
        if ans.days == 1: 
            count += cost
            days += 1
        d1 = d2
        c1 = c2
        n -= 1

    print (days, count)
    
    n = int(input())