d = {"W": 1, "H": 1/2., "Q": 1/4., "E":1/8., "S":1/16., "T":1/32., "X":1/64.}

e = input().split("/")

while e != ["*"]:
    c = 0
    compassos = 0
    for s in e:
        for nota in s: 
            compassos += d[nota]
        if compassos == 1: c += 1
        compassos = 0
    
    print(c)
    e = input().split("/")

