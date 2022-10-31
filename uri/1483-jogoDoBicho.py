import math

v, n, m = raw_input().split()

while(v != "0"):
    v = float(v)

    if(len(n) < 4):
        n = "0"*(4 - len(n)) + n
    if(len(m) < 4):
        m = "0"*(4 - len(m)) + m

    if(n[(len(n) - 4):len(n)] == m[(len(m) - 4):len(m)]):
        print("%.2f" % (v*3000))
    elif(n[(len(n) - 3):len(n)] == m[(len(m) - 3):len(m)]):
        print("%.2f" % (v*500))
    elif(n[(len(n) - 2):len(n)] == m[(len(m) - 2):len(m)]):
        print("%.2f" % (v*50))
    elif(math.ceil(float(n[(len(n) - 2):len(n)])/4) == math.ceil(float(m[(len(m) - 2):len(m)])/4)):
        print("%.2f" % (v*16))
    else:
        print("%.2f" % 0)

    v, n, m = raw_input().split()