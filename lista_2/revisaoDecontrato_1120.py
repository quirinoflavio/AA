d, n = map(str, input().split())
while d != "0" and n != "0":
    n = n.replace(d, "")
    if n=="":
        print(0)
    else:
        print(int(n))
    d, n = map(str, input().split())
