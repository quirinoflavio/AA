import os
a = os.read(0,10000)
print("len a %d" % len(a))
for i in xrange(len(a)):
    if i != a[i]:
        os.sys.stdout.write(a[i])

