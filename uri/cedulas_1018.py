valor = int(input())
print(valor)

cem = int(valor/100)
valor -= cem * 100
print("%d nota(s) de R$ 100,00" % cem)

cinq = int(valor/50)
valor -= cinq * 50
print("%d nota(s) de R$ 50,00" % cinq)

vin = int(valor/20)
valor -= vin * 20
print("%d nota(s) de R$ 20,00" % vin)

dez = int(valor/10)
valor -= dez * 10
print("%d nota(s) de R$ 10,00" % dez)

cinc = int(valor/5)
valor -= cinc * 5
print("%d nota(s) de R$ 5,00" % cinc)

doi = int(valor/2)
valor -= doi * 2
print("%d nota(s) de R$ 2,00" % doi)

um = valor
print("%d nota(s) de R$ 1,00" % um)
