from math import gcd
n = int(input())
a, b = map(int,input().split())
x, y = a, b

for i in range(n-1):
    
    x = max( gcd(x, a), gcd(x, b) )
    y = max( gcd(y, a), gcd(y, b) )
    a, b = map(int,input().split())

x = max( gcd(x, a), gcd(x, b) )
y = max( gcd(y, a), gcd(y, b) )

ans = max(x, y)
if ans == 1: print (-1)
else: print (ans)

