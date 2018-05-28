def lucky_number(n, t):
    for i in range(10**(n)-1, 10**(n-1)-1, -1):
        if i % t == 0:
            return i
    return -1

n, t = map(int, input().split())
if n == 1 and t == 10: print("-1")
else: print(lucky_number(n, t))
