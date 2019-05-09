n, m = map(int, raw_input().split())

board = [ [] for x in xrange(n) ]

for li in xrange(n):
    board[li] = list(raw_input())

g = dict()

for li in xrange(n):
    for col in xrange(m):
        if (li,col) not in g:
            g[(li,col)] = []
        

        if (col < m-1) and (col > 0):
            g[ (li,col) ].append( (li,col + 1) )
            g[ (li,col) ].append( (li,col - 1) )
        elif (col == m):
            g[ (li,col) ].append( (li,col - 1) )
        else:
            g[ (li,col) ].append( (li,col + 1) )
        

        if (li > 0) and (li < n-1):
            g[ (li,col) ].append( (li + 1,col) )
            g[ (li,col) ].append( (li - 1,col) )
        elif (li == 0):
            g[ (li,col) ].append( (li + 1,col) )
        else:
            g[ (li,col) ].append( (li - 1,col) )
            

def up((x, y)):
    if x > 0:
        return (x-1, y)

def down((x, y)):
    if x < n-1:
        return (x+1, y)

def left((x, y)):
    if y > 0:
        return (x, y-1)

def right((x, y)):
    if y < m-1:
        return (x, y+1)
ans = False

def gg(tupla, contador, conj):
    if contador >= 4 and tupla in conj:
        ans = True
        print "2134EDFSFDF"
        return 
    conj.add(tupla)
    for t in g[tupla]:
        gg(t, contador+1, conj)
    

print ans
print g
gg( (0,0), 0, set())