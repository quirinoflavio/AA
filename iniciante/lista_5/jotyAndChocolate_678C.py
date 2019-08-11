n,a,b,p,q = map(int, input().split())

result = 0
if n%a==0 and n%b == 0:
    dab = min(n//a, n//b)
else:
    dab = n//(a*b)
da = n//a
db = n//b

if max(p,q)==q:
    result += dab*q
else:
    result += dab*p

result += (da-dab)*p
result += (db-dab)*q
print(dab,da,db)
print(result)
