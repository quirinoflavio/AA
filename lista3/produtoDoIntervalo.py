while True:
    try:
        N, K = map(int, raw_input().split())
        array = map(int, raw_input().split())

        for i in xrange(K):
            op, i, x = raw_input().split()
            i, x = int(i), int(x)
            if op == "C":
                update(i, x)
            else:
                query(i)
    except EOFError:
        break

def update():
    return 0