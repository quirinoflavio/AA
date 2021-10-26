# INCOMPLETE

from collections import defaultdict
num = int(raw_input())
origin = map(int, raw_input().split())
destiny = map(int, raw_input().split())
land = [ map(int, list(raw_input())) for x in xrange(num)]

def matrix_to_list(am):
    al= {} #doesnt contain path from a node to itself.
    for x, row in enumerate(am):
        al[x+1]=[]
        for i, v in enumerate(row):
            if v== 1 and i!=x:
                al[x+1].append(i+1)
    print(al)

def cost(t1, t2):
    return (t1[0] - t2[0])**2 + (t1[1] - t2[1])**2

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

matrix_to_list(land)