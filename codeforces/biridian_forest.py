from collections import defaultdict as dd, deque, Counter as C
import sys
 
def data(): 
    return sys.stdin.readline().strip()
 
def out(*var, end="\n"): 
    sys.stdout.write(' '.join(map(str, var)) + end)
 
def L(): 
    return list(sp())
 
def sl(): 
    return list(ssp())
 
def sp(): 
    return map(int, data().split())
 
def ssp(): 
    return map(str, data().split())
 
def l1d(n, val=0): 
    return [val for i in range(n)]
 
def l2d(n, m, val=0): 
    return [l1d(n, val) for j in range(m)]
 
def A2(n,m): 
    return [[0] * m for i in range(n)]
 
def A(n):
    return [0] * n
 
r, c = L()
 
A = [list(input()) for i in range(r)]
 
start = []
end = []
occs = []
for i in range(r):
        for j  in range(c):
                if A[i][j] == "S":
                        start = [i, j]
                elif A[i][j] == "E":
                        end = [i,j]
                elif A[i][j] not in "0T":
                        occs.append([i, j])
 
q = deque()
q.append([end[0], end[1], 0])
vis = [[-1 for i in range(c)] for j in range(r)]
 
while(q):
        x,y,d = q.popleft()
        vis[x][y] = d
        row = [-1, 0, 0, 1]
        col = [0, -1, 1, 0]
        for k in range(4):
                a = x + row[k]
                b = y + col[k]
                if 0 <= a < r and 0 <= b < c and vis[a][b] == -1 and A[a][b] != "T":
                        vis[a][b] = d + 1
                        q.append([a, b, d + 1])
 
x, y = start
final_time = vis[x][y]
fight = 0
for i in range(r):
        for j in range(c):
                if A[i][j] not in "SET0" and vis[i][j] <= final_time and vis[i][j] != -1:
                        fight += int(A[i][j])
 
print(fight)