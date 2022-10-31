num = input()

cont = 0


while True:
  f = 1
  i = 1
  while f < num:
    f *= i
    i += 1
  cont += 1
  
  if f > num:
    f = f / (i-1)
    num -= f

  elif f == num: break

print cont