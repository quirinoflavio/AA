import math
def divisores(num):
    i = 2
    lista = []
    while i <= num//2:
        if num/i == num//i:
            lista.append(i)
        i+=1
    return lista
def lovely(div, num):
    for i in div:
        if (i*i) % num == 0: return -1
    return num
def lvly(div, num, ans):
    if ans == -1:
        return ggwp(div[:-1],div[-1])
    else:
        return num
def ggwp(div, num):
    return lvly(div, num, lovely(div, num))
num = int(input())
lista = divisores(num)
r = ggwp(lista, num)
print(r)
