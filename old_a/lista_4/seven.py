import os;from sys import stdin, stdout;l=['1\n','7\n','9\n','3\n'];d = os.read(0,1000000000)
for i in xrange(2,len(d),2):
    print(d[i])
    #if i>=0  and i<=1000000000:
    #stdout.write(l[int(d[i])&3])
