from Queue import Queue

def buildGraph():
    graph = dict()
    noVert = int(raw_input())
    noEdges = int(raw_input())

    #vert = map(int, raw_input().split())
    #for v in vert:
    #    graph[v] = []

    for v in xrange(1, noVert+1):
        graph[v] = []

    for e in range(noEdges):
        x, y = map(int, raw_input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    return graph

#ta errado, muito
def eulerTour(graph, n, v, q, c):
    if v > n: return  eulerTour(graph, n, -1, q, False)
    if c:
        q.put(v)
        return str(v) + " " +  eulerTour(graph, n, graph[v][0], q, c)
    if not q.empty():
        elem = q.get()
        return eulerTour(graph, n, v, q, c) + " " + str(elem)
    return ""

def euler(graph, a, v, s, path):
    if len(path) == len(graph)*2: return path
    if graph[v] and v != a:
        s.append(v)
        path.append(v)
        graph[v].remove(a)
        for c in reversed(graph[v]):
            s.append(c)
        nv = s.pop()
        return euler(graph, v, nv, s, path)
    else:
        path.append(v)
        nv = s.pop()
        return euler(graph, a, nv, s, path)
    
def eulerPath(graph):
    
    stack = [ 1 ]
    path = []
    
    # main algorithm
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v][0]
            stack.append(u)
            # deleting edge u-v
            del graph[u][ graph[u].index(v) ]
            del graph[v][0]
        else:
            path.append( stack.pop() )
    
    return path
    



def main():
    #graph = buildGraph()
    #print graph
    gr = {1:[2, 3], 2:[1], 3:[1, 4, 5], 4:[3], 5:[3, 6], 6:[5, 7], 7:[6]}
    #gr2 = { 1:[2,3], 2:[1,3,4,5], 3:[1,2,4,5], 4:[2,3,5], 5:[2,3,4] }
    #print eulerPath(gr)
    #print eulerPath(gr2)
    print euler(gr, -1, 1, [], [])

main()