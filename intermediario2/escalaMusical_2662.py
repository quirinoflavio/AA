#Nâo terminada
# do do# re re# mi fa fa# sol sol# la la# si
#  1  2   3  4   5  6  7   8    9  10 11 12

mapa = {1: "do", 2: "do#", 3: "re", 4: "re#", 5: "mi", 6:"fa", 7:"fa#", 8:"sol", 9:"sol#", 10:"la", 11:"la#", 12:"si"}


n = int(raw_input())
acordes = []
for i in xrange(n):
    acorde = int(raw_input()) - 1
    acordes.append(acorde)
d = False
menor = 13
for i in xrange(n-1):
    if (i % 7 == 0):
        if i % 7 < menor: menor = i % 7
    if ((i % 7 == 0) or (i % 7 == 1) or (i % 7 == 3) or (i % 7 == 4) or (i % 7 == 5)) and\
        abs((acordes[i]%12) - acordes[i+1]%12) == 2: continue
    #(( (acordes[i] % 12) > (acordes[i+1] % 12) and ((acordes[i+1] % 12) - (acordes[i] % 12) ==-2) ) or\
    #( (acordes[i] % 12) < (acordes[i+1] % 12) and ((acordes[i+1] % 12) - (acordes[i] % 12) == 2) )): continue
        
    elif ((i % 7 == 2) or (i % 7 == 6)) and \
        abs((acordes[i]%12) - (acordes[i+1]%12)) == 1 or\
        (((acordes[i+1]%12) < (acordes[i]%12)) and (abs((acordes[i]%12) - (acordes[i+1]%12)) == 11)): continue 

    #(( (acordes[i] % 12) > (acordes[i+1] % 12) and ((acordes[i+1] % 12) - (acordes[i] % 12) ==-1) ) or\
    #( (acordes[i] % 12) < (acordes[i+1] % 12) and ((acordes[i+1] % 12) - (acordes[i] % 12) == 1) )): continue
        
    else: 
        print i%7, acordes[i], acordes[i+1], acordes[i+1]%12 - acordes[i]%12
        d = True

if not d:
    print mapa[menor + 1]
else:
    print "desafinado"