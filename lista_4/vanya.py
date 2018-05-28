e = int(input())
i = 0
val = 1
res = 0

while i <= 9 and e >= val:
    res += e - val + 1
    val *= 10
    i += 1

print(res)
