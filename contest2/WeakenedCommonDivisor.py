from math import gcd
n = int(input())
#a, b = map(int,input().split())
#x, y = a, b


def haha(x, y, n, k):
    print (n)
    if n == 1:
        return max(x,y)
    a, b = map(int,input().split())
    if n == k: x, y = a, b
    gx = gcd(x, a), gcd(x, b)
    gy = gcd(y, a), gcd(y, b)

    return max(haha(min(gx),min(gy), n-1, -1), haha(min(gx), max(gy), n-1, -1), haha(max(gx), min(gy), n-1, -1), haha(max(gx), max(gy), n-1, -1) )

print (haha(0, 0, n, n))
"""
for i in range(n-1):
    
    x = max( gcd(x, a), gcd(x, b) )
    y = max( gcd(y, a), gcd(y, b) )
    a, b = map(int,input().split())

x = max( gcd(x, a), gcd(x, b) )
y = max( gcd(y, a), gcd(y, b) )

ans = max(x, y)
if ans == 1: print (-1)
else: print (ans)

"""