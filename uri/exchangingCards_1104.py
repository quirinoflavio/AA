while True:
    a, b = map(int, raw_input().split())
    if (a == 0 and b == 0): break
    
    ca = list(set(map(int, raw_input().split())))
    cb = list(set(map(int, raw_input().split())))

    ta = len(ca)
    tb = len(cb)

    ma = [0 for i in xrange(100001)]
    for i in xrange(ta): ma[ca[i]] = 1

    mb = [0 for i in xrange(100001)]
    for i in xrange(tb): mb[cb[i]] = 1

    cta = 0
    for i in xrange(ta):
        if (not mb[ca[i]]):
            cta += 1

    ctb = 0
    for i in xrange(tb):
        if (not ma[cb[i]]):
            ctb += 1

    print min(ctb, cta)