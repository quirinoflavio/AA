from math import factorial as fa

a, b, n = map(int, raw_input().split())
def modu(n):
    return n % 1000000007



def calc(a, b, n):
    i = n
    f = 0
    soma = 0
    while i >= 0 and f <= n:
        numero = a*i + b*f
        if isB(str(a), str(b), str(numero)):
            soma += qntd(i, f)
            soma = modu(soma)
        i -= 1
        f += 1
    return soma


def qntd(i, f):
    return modu(fa(i+f)) / ( modu( modu((fa(i)) * modu(fa(f))) + 0.0))

def isB(a, b, n):
    for i in n:
        if i != a and i != b:
            return False
    return True

print calc(a, b, n)