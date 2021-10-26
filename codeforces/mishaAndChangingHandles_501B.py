numR = int(input())

dic ={}

for i in range(numR):
    old, new = input().split()
    if old not in dic:
        dic[new] = old
    else:
        aux = dic.pop(old)
        dic[new] = aux

print(len(dic))
for key in dic:
    print(dic[key], key)

