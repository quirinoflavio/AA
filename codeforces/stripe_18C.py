n = int(input())
squares = list(map(int, input().split()))

cortes = 0

ia, ib = 0, 0

	
soma_esq = squares[0]
soma_dir = 0

for i in range(1, len(squares)):
	soma_dir += squares[i]

for j in range(1, len(squares)):
    if soma_dir == soma_esq:
        cortes += 1
    soma_dir -= squares[j]
    soma_esq += squares[j]
    
		
print(cortes)
