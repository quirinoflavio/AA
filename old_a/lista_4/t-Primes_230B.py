s = set()
LIM = 1000001
def montaP(s):
    p = [1]*LIM
    for i in range(2, LIM):
        if p[i]:
            s.add(i*i)
            for k in range(2*i, LIM, i):
                p[k] = 0
montaP(s)
n = int(input())
l = map(int, input().split())
for i in l:
    print("YES") if i in s else print("NO")
