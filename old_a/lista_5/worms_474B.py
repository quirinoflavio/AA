from sys import stdin, stdout

qp = int(stdin.readline())
pilhas = list(map(int, stdin.readline().split()))
qw = int(stdin.readline())
w = list(map(int, stdin.readline().split()))
cp = sorted(w)
p = {}

qa = 0
pa = 0
for i in range(qw):
    while pa < qp:
        qa += pilhas[pa]
        if cp[i] <= qa:
            p[cp[i]]=pa+1
            pa += 1
            break
        pa += 1
for i in w:
    print(p[i])
