n,a,b = map(int, input().split())
b+=1
fila = [1]*n
for i in range(n-1-b, -1, -1):
    fila[i] = 0
for i in range(a):
    fila[i] = 0
cont = 0
i=n-1
while i >= 0:
    if fila[i] == 1:
        cont+=1
        i -= 1
    else: break

print(cont)
