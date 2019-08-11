#l=['1\n','7\n','9\n','3\n']
from sys import stdin, stdout;l=['1\n','7\n','9\n','3\n'];
for i in xrange(int(stdin.readline())): stdout.write(l[int(stdin.readline())&3])


#r = int(stdin.readline());
#l=['1\n','7\n','9\n','3\n']
#for i in xrange(r):
#    n = int(stdin.readline())
#    stdout.write(l[n&3])
