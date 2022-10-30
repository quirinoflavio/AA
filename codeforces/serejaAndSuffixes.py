n, m = map(int, raw_input().split())
 
array = map(int, raw_input().split())
cont = [0]*n
conj = set()
 
conj.add(array[-1])
cont[n-1] = 1
 
for i in range(n-2, -1, -1):
  tam = len(conj)
  conj.add(array[i])
  if len(conj) > tam:
    cont[i] = cont[i+1] + 1
  else:
    cont[i] = cont[i+1]
 
 
for i in range(m):
  print cont[input()-1]