fb, d, bw = map(int, raw_input().split())
soma = int((1 + bw)*bw*fb/2.) - d
if soma > 0:print soma
else: print 0