e = input()
c = 0
if c[-1] = 0:
    c+= 9
else:
    c+= int(c[-1])

for i in range(len(e)-2, -1, -1):
    if c[i] == 0:
        c+= ((9*10**(i-1))*(i+1))

    else:
        c+= 
