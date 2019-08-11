n = int(raw_input())
array = map(int, raw_input().split())

countF = [-1]*1000001
countB = [-1]*1000001

j = n-1
for i in xrange(n):
    if countF[array[i]] == -1: countF[array[i]] = i+1
    countB[array[i]] = j+1
    j -= 1

qn = int(raw_input())
queries = map(int, raw_input().split())

somaF = 0
somaB = 0

for i in queries:
    if countF[i] != -1: somaF += countF[i]
    if countB[i] != -1: somaB += countB[i]

print somaF, somaB
