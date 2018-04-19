n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = a.copy()
cb = b.copy()

ca.sort()

ia = 0
ib = 0

qntd = 0
saida = [0] * len(cb)
saida2 = [0] * len(cb)

while(ia < len(ca) and ib < len(cb)):
	
	if cb[ib] >= ca[ia]:
		qntd += 1
		ia += 1
	else:
		saida[ib] += qntd
		if ia < len(b):
			if cb[ib] == b[ia]:
				print(cb[ib], b[ia])
				saida2[ia] = saida[ib]
		ib +=1
		
saida[-1] = qntd


print (saida)
print (saida2)
