n, k, x = map(int, input().split())

balls = list(map(int, input().split()))


def conta_pares(vet, num):
    pares = []
    for i in range(n-1):
        if balls[i] == balls[i+1] == num:
            pares.append(i)
    return pares


# 1 1 2 2 1 1
def calc_pontos(vet, par):
    pontos = 2
    l, r = par[0], par[1]
    while l >= 0 and r < len(vet):
        if vet[l-1] == vet[r+1]:
            l -= 2
            r -= 2
            if vet[l]
