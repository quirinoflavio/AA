import math
def fat(n):
    return math.factorial(n)
n,m,t=map(int, input().split())

print((fat(n)//fat(t-1)*fat(n-(t-1)))*m)
