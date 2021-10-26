import math
num = int(input())
res = 1
first = 0
 
while num%2==0:
    if first == 0:
        res*=2
        first=1
    num= num//2
 
for i in range(3, int(math.sqrt(num))+1, 2):
    first = 0
    while num%i == 0:
        if first == 0:
            res*=i
            first = 1
        num = num//i
 
if num>2: res*=num
 
print(res)
