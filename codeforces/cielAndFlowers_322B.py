r, g, b = map(int, input().split())
total = 0
while r!=0 and g!=0 and b!=0:
    total += 1
    r-=1; g-=1; b-=1
tr = r // 3
r -= tr * 3

tg = g // 3
g -= tg * 3

tb = b // 3
b -= tb * 3

total += tr + tg + tb

print(total)
