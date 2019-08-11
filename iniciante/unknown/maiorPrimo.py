def maior_Primo(n):
    aux = n
    while aux > 2:
        if ehPrimo(aux):
            return aux
        aux -= 1
    return 2
def ehPrimo(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True
num = int(input())
for i in range(num):
    print(maior_Primo(int(input())))
