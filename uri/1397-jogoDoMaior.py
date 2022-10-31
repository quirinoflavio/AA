n = int(input())

while(n != 0):
  resA = 0
  resB = 0

  for i in range(n):
    a, b = map(int, input().split())

    if(a > b):
      resA += 1
    elif(b > a):
      resB += 1

  print(resA, resB)
  n = int(input())