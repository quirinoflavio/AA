# WA

n = int(raw_input())
t = raw_input()

qG = 0
qT = 0
mSub = 0
sub = 0
cSub = 0
for i in xrange(n):
    if t[i] == "G": 
        sub += 1
        qG += 1
    else:
        qT += 1
        if sub > mSub:
            mSub = sub
            for j in xrange(i+1, n):
                if t[j] == "G": 
                    sub += 1
                else:
                    if sub > cSub:
                        cSub = sub
                        break
            sub = 0

if cSub > mSub and qT > 1 and qG > cSub:
    print cSub+1
elif cSub > mSub and qT > 1 and qG == cSub:
    print cSub
else:
    if mSub == 0:
        print sub
    else:
        print mSub
    