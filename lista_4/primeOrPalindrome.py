import time

def isPalindrome(num):
    if num == int(str(num)[::-1]): return 1
    return 0


def preC(num_palin, num_primos, LIM):
    isPrime=[1]*(LIM+1)
    isPrime[0], isPrime[1] = 0, 0
    for i in range(2,LIM+1):
        if isPrime[i]:
            for j in range(2*i, LIM+1, i):
                isPrime[j] = 0

    for i in range(1, LIM+1):
        num_primos[i] = num_primos[i-1] + isPrime[i]
        num_palin[i] = num_palin[i-1] + isPalindrome(i)


LIM = 1000000
num_primos=[0]*(LIM+1)
num_palin=[0]*(LIM+1)

preC(num_palin,num_primos,LIM)
p, q = map(int, input().split())
a = p/q
ai = p//q

for i in range(LIM, 0, -1):
    if num_primos[i] < a*num_palin[i]:
        print(i)
    else: break

