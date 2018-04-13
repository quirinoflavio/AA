qt = 0
while(True):
    iv = int(input())
    if iv == 0: break;
    oc = list(map(int, input().split()))
    for i in range(iv):
        if oc[i] == i+1:
            qt += 1
            print("Teste %d" % qt)
            print(oc[i])
            print()
            break;
