def e_mdc(d1, d2):
    if d2 == 0:
        return d1
    return e_mdc(d2, d1%d2)
d1, d2 = map(int, input().split())
print(e_mdc(d1, d2))
