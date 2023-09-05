import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(input()))
    

cnt = 0

def dfs(graph,x, y):
    global cnt
    
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    if graph[x][y] == 'X':
        return False
    if graph[x][y] == 'V':
        return False
    
    if graph[x][y] == 'P':
        cnt += 1
    graph[x][y] = 'V'


    dfs(graph, x-1, y)
    dfs(graph, x+1, y)
    dfs(graph, x, y-1)
    dfs(graph, x, y+1)
   

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            dfs(graph, i, j)
            break

if cnt == 0:
    print('TT')
else:
    print(cnt)