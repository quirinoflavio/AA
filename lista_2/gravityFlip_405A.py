num_col = int(input())
cubos = list(map(int, input().split()))

cubos.sort()

for i in range(0, len(cubos)-1):
	print(cubos[i], end=" ")

print(cubos[-1])
