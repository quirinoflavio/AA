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
    

def main():
    graph = buildGraph()
    print graph
    print eulerTour(graph, len(graph), 1, Queue(), True)


main()