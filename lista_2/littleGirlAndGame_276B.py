s = input()

a = ord("a")
letras= [0] * 26

for l in s:
	letras[ord(l) - a] += 1
	

qntd_sem_par = 0

for i in letras:
	if i%2 == 1:
		qntd_sem_par += 1


if qntd_sem_par == 0:
	print("First")
elif qntd_sem_par%2 == 0:
	print("Second")
else:
	print("First")
