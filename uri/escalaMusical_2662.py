# do do# re re# mi fa fa# sol sol# la la# si
#  0  1   2  3   4  5  6   7    8   9  10 11

mapa = {0: "do", 1: "do#", 2: "re", 3: "re#", 4: "mi", 5:"fa", 6:"fa#", 7:"sol", 8:"sol#", 9:"la", 10:"la#", 11:"si"}

do = [0,2,4,5,7,9,11];doS = [1,3,5,6,8,10,0];re = [2,4,6,7,9,11,1];reS = [3,5,7,8,10,0,2]
mi = [4,6,8,9,11,1,3];fa = [5,7,9,10,0,2,4];faS = [6,8,10,11,1,3,5];sol = [7,9,11,0,2,4,6]
solS = [8,10,0,1,3,5,7];la = [9,11,1,2,4,6,8];laS = [10,0,2,3,5,7,9];si = [11,1,3,4,6,8,10]

n = int(raw_input())
tons = [True for x in xrange(12)]

for i in xrange(n):
    acorde = (int(raw_input()) -1) % 12
    
    if acorde not in do: tons[do[0]] = False
    if acorde not in doS: tons[doS[0]] = False
    if acorde not in re: tons[re[0]] = False
    if acorde not in reS: tons[reS[0]] = False
    if acorde not in mi: tons[mi[0]] = False
    if acorde not in fa: tons[fa[0]] = False
    if acorde not in faS: tons[faS[0]] = False
    if acorde not in sol: tons[sol[0]] = False
    if acorde not in solS: tons[solS[0]] = False
    if acorde not in la: tons[la[0]] = False
    if acorde not in laS: tons[laS[0]] = False
    if acorde not in si: tons[si[0]] = False


print mapa[tons.index(True)] if True in tons else "desafinado"
