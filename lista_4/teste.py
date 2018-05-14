import math
LIMITE = 2147483648
#LIMITE = 300
RAIZ = int(math.sqrt(LIMITE))
print(RAIZ==46340)
#RAIZ = 30
vetor = [1 for i in range(2, RAIZ+1)]

for i in range(2, RAIZ):
    if vetor[i] == 1:
        for j in range(i*i, RAIZ, i):
            vetor[j] = 0

for i in range(int(input())):
    if vetor[int(input())]:
        print("Prime")
    else:
        print("Not Prime")
