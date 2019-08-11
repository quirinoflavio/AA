n = int(raw_input())
s = raw_input()

array = [(0, 0)]*(n+1)
counter = [0] * 26

for j in xrange(n):
    counter[ord(s[j]) - 97] += 1
    array[j] = (j, counter[ord(s[j])-97])
    
q = int(raw_input())

for i in xrange(q):
    ss = raw_input()
    
