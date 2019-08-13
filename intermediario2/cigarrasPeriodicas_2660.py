##TLE
n, l = map(int, raw_input().split())

population = map(int, raw_input().split())

def mmc(num1, num2):
    a = num1
    b = num2
    ca = a
    cb = b
    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return (num1 * num2) / a

current_mmc = 1
for i in xrange(n):
    current_mmc = mmc(population[i], current_mmc)

x = 1
max_mmc = current_mmc
for i in xrange(2, l+1):
    new_mmc = mmc(current_mmc, i)
    if new_mmc > max_mmc and new_mmc <= l:
        max_mmc = new_mmc
        x = i

print x 