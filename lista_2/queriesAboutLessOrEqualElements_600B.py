n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

def busca_binaria(vetor, num):
    esquerda, direita = 0, len(vetor)
    while esquerda<=direita:
        meio = (esquerda+direita) // 2

        if esquerda == direita:
            return esquerda

        aux_num = vetor[meio]

        if num == aux_num:
            return meio+1
        elif num > aux_num:
            esquerda = meio+1
        else:
            direita = meio

for i in range(0, len(b)-1):
    print(busca_binaria(a, b[i]), end=" ")

print(busca_binaria(a, b[-1]))
