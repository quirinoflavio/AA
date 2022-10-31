n = int(input())

for i in range(n):
  ent = input()

  if(ent[0] == ent[2]):
    print(int(ent[0]) * int(ent[2]))
  elif(ent[1] == ent[1].lower()):
    print(int(ent[0]) + int(ent[2]))
  elif(ent[1] == ent[1].upper()):
    print(int(ent[2]) - int(ent[0]))