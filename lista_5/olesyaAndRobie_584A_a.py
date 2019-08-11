n, t = map(int, input().split())
result = "1"
x = n
if t == 10 and n == 1: print(-1)
elif n == 1: print(t)
else:
    if t != 10:
        result = str(t)
    elif t == 10: n-=1
    for i in range(n-2):
        result+="0"

    a =result+str(t)
    if x == 2 and t == 10: a = a[1:]
    print(a)
