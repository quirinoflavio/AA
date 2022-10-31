s = raw_input()

while(s != "*"):
    l = s.split()
    ok = True
    aux = l[0][0].lower()

    for i in xrange(1, len(l)):
        if(l[i][0].lower() != aux):
            ok = False
            break

    if(ok):
        print("Y")
    else:
        print("N")

    s = raw_input()