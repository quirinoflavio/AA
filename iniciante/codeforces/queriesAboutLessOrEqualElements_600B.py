n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
uva = b.copy()
b.sort()

ia, ib = 0, 0

qntd = 0
dic = {}

while ia <= n and ib < m:
    if ia == n:
        dic[b[ib]] = qntd
        ib += 1
    elif b[ib] >= a[ia]:
        qntd += 1
        ia += 1
    else:
        dic[b[ib]] = qntd
        ib += 1


for i in range(m-1):
    print(dic[uva[i]], end=" ")
print(dic[uva[-1]])
