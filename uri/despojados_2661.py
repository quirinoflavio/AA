n = int(raw_input())


divisores = set()
d = 2
sqrt = (n**(0.5) + 1)
while(n > 1):
    if d > sqrt: break
    while (not n%d):
        n /= d
        divisores.add(d)
    d += 1

if n != 1:
    divisores.add(n)
print 2**len(divisores) - len(divisores) - 1