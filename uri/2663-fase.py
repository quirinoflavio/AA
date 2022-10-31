num = int(input())
lim = int(input())

comp = []

for i in range(num):
  comp.append(int(input()))

comp.sort(reverse=True)

last = comp[0]
cont = 0
for i in range(lim):
  last = comp[i]
  cont += 1
  i += 1

while(i < num and comp[i] == last):
  cont += 1
  i += 1

print(cont)