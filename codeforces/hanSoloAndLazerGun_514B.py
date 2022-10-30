n, x0, y0 = map(int, raw_input().split())
lista = [-1]*n
for i in range(n):
  lista[i] = map(int, raw_input().split())
 
conj = set()
for i in range(n):
  x = lista[i][0]
  y = lista[i][1]
  if x == x0:
    conj.add(123321123)
  elif y == y0:
    conj.add(890098890)
  else:
    conj.add((y - y0) / ((x-x0) * 1.0))
 
print len(conj)