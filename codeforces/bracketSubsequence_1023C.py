n, k = map(int, raw_input().split())
brackets = list(raw_input())
 
oppened = 0
closed = 0
new = ""
 
for b in brackets:
    if oppened == k/2: break
    if b == "(":
        oppened += 1
        new += "("
    else:
        new += ")"
        closed += 1
 
p = k - len(new)
for i in xrange(p):
    new += ")"
 
print new