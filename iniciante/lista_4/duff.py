def divisores(num):.
    i = 1
    lista = []
    while i <= num//2:
        if num/i == num//i:
            lista.append(i)
        i+=1
    lista.append(num)
    return lista


def lovely(a, left, right):
    if left >= right:
        return a[right]
    c = 1
    p = left
    e = a[right]
    while p < right and c:
        if a[p]**2 % e == 0 or e % a[p]**2 == 0:
            c = 0
        p += 1
    if c:
        return e
    else:
        b = divisores(a[right-1])
        return lovely(b, left, len(b)-1)

def lvly(n, l):
    for i in l:
        if n % i == 0:
            return lvly(l[-1], div(l[-1])

#12 - 1 2 3 6 12
#6  - 1 2 3 6
