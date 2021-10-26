num_cities = int(input())

c = list(map(int, input().split()))

print(abs(c[0] - c[1]), abs(c[0] - c[-1]))

for i in range(1, len(c)-1):

    med = min(abs(c[i]-c[i-1]), abs(c[i]-c[i+1]))
    mad = max(abs(c[i]-c[0]), abs(c[i]-c[-1]))

    print(med, mad)

print(abs(c[-1]-c[-2]), abs(c[-1]-c[0]))
