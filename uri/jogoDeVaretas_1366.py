n = int(input())

while(n != 0):
  res = 0
  for i in range(n):
    c, v = map(int, input().split())

    res += int(v/2)

  print(int(res/2))
  n = int(input())