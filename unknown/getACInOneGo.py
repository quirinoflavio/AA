from fractions import gcd
from sys import stdin, stdout

stdin.next()

for line in stdin:
    a, b = map(int, line.split())
    stdout.write(str(a*b-a-b+1)+'\n') if (gcd(a,b) == 1) else stdout.write("-1\n")