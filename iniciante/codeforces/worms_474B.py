def acc_sum(array):
    for i in xrange(1, len(array)):
        array[i] += array[i-1]
 
def bin_search(e, array, l, r):
    middle = (l+r)//2
    if array[middle] == e: return middle+1
    if l >= r: return r+1
    if array[middle] < e:
        return bin_search(e, array, middle+1, r)
    return bin_search(e, array, l, middle)
 
qp = input()
pilhas = map(int, raw_input().split())
qw = input()
worms = map(int, raw_input().split())
 
acc_sum(pilhas)
for i in worms:
    a = bin_search(i, pilhas, 0, qp-1)
    print(a)
