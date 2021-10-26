import time
def sum(p, q):
    r = 0
    for i in range(len(p)):
        #xor entre substringB[i] e a[i]
        r += int(p)^int(q)
    return r

a = input() #string a
b = input() #string b
tam_a=len(a) #tamanho a
tam_b=len(b) #tamanho b

result = 0

for i in range(tam_b):
    if tam_a+i> tam_b: break #condicao de parada
              #soma substring de b com s
    result += (sum(b[i:tam_a+i], a))
print(result)
