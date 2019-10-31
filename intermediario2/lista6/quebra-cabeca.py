from collections import Counter as cn

l, c = map(int, raw_input().split())
lis = []
res = dict()

for i in xrange(l+1):
    lis.append(raw_input().split())

for i in xrange(c):
    tmp = []
    for j in xrange(l+1):
        tmp.append(lis[j][i])
    lis.append(tmp)

lis.pop(l)

for i in xrange(l):
    lis[i] = [dict(cn(lis[i][:c])), int(lis[i][c])]

for i in xrange(l, l+c):
    lis[i] = [dict(cn(lis[i][:l])), int(lis[i][l])]

while(len(lis) > 0):
    k = 0

    for i in xrange(len(lis)):
        if(len(lis[i][0]) == 1):
            k = i
            break

    nm = lis[i][0].keys()[0]
    v = lis[i][1] / lis[i][0][nm]
    res[nm] = v
    
    lis.pop(i)
    rm = []

    for i in xrange(len(lis)):
        if(nm in lis[i][0].keys()):
            lis[i][1] -= v * lis[i][0][nm]
            del lis[i][0][nm]

            if(len(lis[i][0]) == 0):
                rm.append(i)

    rm.sort(reverse = True)

    for i in xrange(len(rm)):
        lis.pop(rm[i])

tres = sorted(res.keys())

for k in tres:
    print k, res[k]