s1 = input()
s2 = input()

TAM = 26

a_min = ord("a")
a_mai = ord("A")

ls1_min = [0]*TAM
ls1_mai = [0]*TAM
ls2_min = [0]*TAM
ls2_mai = [0]*TAM

for letra in s1:
    if letra.islower():
        ls1_min[ord(letra) - a_min] += 1
    else:
        ls1_mai[ord(letra) - a_mai] += 1

for letra in s2:
    if letra.islower():
        ls2_min[ord(letra) - a_min] += 1
    else:
        ls2_mai[ord(letra) - a_mai] += 1

yay = 0
whoops = 0

for letra in range(TAM):
    casos = min(ls1_min[letra], ls2_min[letra])
    yay += casos
    ls1_min[letra] -= casos
    ls2_min[letra] -= casos

    casos = min(ls1_mai[letra], ls2_mai[letra])
    yay += casos
    ls1_mai[letra] -= casos
    ls2_mai[letra] -= casos

for letra in range(TAM):
    casos = min(ls1_min[letra], ls2_mai[letra])
    casos += min(ls1_mai[letra], ls2_min[letra])
    whoops += casos

print(yay, whoops)
