def ver_ant(array, left, i, e):
    if i-1 >= left and array[i-1] == e:
        return ver_ant(array, left, i-1, e)
    return i

def b_s(array, left, right, e):
    i = (left+right) // 2
    if array[i] == e:
        return ver_ant(array, left, i, e)
    if left >= right:
        return -1
    elif array[i] > e:
        return b_s(array, left, i-1, e)
    else:
        return b_s(array, i+1, right, e)

n, q = map(int, input().split())
casos= 1
while n != 0 and q != 0:
    array = [0] * n
    for i in range(n):
        array[i] = int(input())

    array.sort()
    print("CASE# %d:" % casos)

    for i in range(q):
        query = int(input())
        saida = b_s(array, 0, n-1, query) +1
        if saida > 0:
            print("%d found at %d" % (query, saida))
        else:
            print("%d not found" % query)

    n, q = map(int, input().split())
    casos += 1
