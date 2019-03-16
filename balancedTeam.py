n=int(raw_input())
l=map(int,raw_input().split())

l.sort()

i = 0
j = 1

tmp = 1
maxi = 0;

while (i < n and j < n):
    if (abs(l[i] - l[j]) <= 5):
        tmp += 1
        j += 1
    else: 
        if (tmp > maxi):
            maxi = tmp
        if (i == j):
            j += 1
        i += 1
        tmp = j - i
        

if (tmp > maxi): maxi = tmp
print maxi



























"""
tmp = 1
maxi = 0
print len(l)

for i in xrange(n):
    j = 1
    while(((i+j) < n) and ((l[i+j] - l[i]) <= 5)):
        
        j += 1
        tmp += 1
    if(tmp > maxi): maxi = tmp
    tmp = 1
    
print(maxi)
"""
