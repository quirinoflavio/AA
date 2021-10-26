## INCOMPLETE

from collections import defaultdict
n, m = map(int, raw_input().split())

board = [ list(raw_input()) for x in xrange(n) ]

visited = set()

graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def matrix_to_list(matrix):
    graph = defaultdict(set)
    for x in xrange(n):
        for y in xrange(m):
            color = matrix[x][y]
            if x>0:
                nc = matrix[x-1][y] 
                graph[(color, (x, y))].add( (nc,(x-1, y)))
            if x < n-1:
                nc = matrix[x+1][y]
                graph[ (color, (x, y))].add((nc, (x+1, y)))
            if y > 0:
                nc = matrix[x][y-1] 
                graph[ (color, (x, y))].add( (nc, (x, y-1)))
            if y < m-1: 
                nc = matrix[x][y+1]
                graph[ (color, (x, y))].add((nc, (x, y+1)))
    return graph

graph = matrix_to_list(board)

def dfs(graph, node, visited, color):
    
    inVisited = node in visited
    if inVisited and node[0] == color:
        visited.append(node)
    elif not inVisited and node[0] == color:
        print node
        visited.append(node)

        for n in graph[node]:
            dfs(graph,n, visited, color)
    
    return len(visited), len(set(visited))
"""
3 4
ABCD
FGHJ
TYUI

3 4
AAAA
BBHJ
TYUI
"""

visited = dfs(graph,('A', (0,0)), [], 'A')
print(visited)





















"""
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
        elif (col == 0):
            g[ (li,col) ].append( (li,col + 1) )
        

        if (li > 0) and (li < n-1):
            g[ (li,col) ].append( (li + 1,col) )
            g[ (li,col) ].append( (li - 1,col) )
        elif (li == 0):
            g[ (li,col) ].append( (li + 1,col) )
        elif (li == n):
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
        print ans
    else:
        conj.add(tupla)
        for t in g[tupla]:
            gg(t, contador+1, conj, ans)
    

print g
print "$$$$"
gg( (0,0), 0, set(), ans)

print ans"""