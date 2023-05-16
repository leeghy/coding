from collections import deque

N, M, start = map(int, input().split())

graph_dfs = [[] for _ in range(N+1)]
graph_bfs = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph_dfs[x].append(y)
    graph_dfs[y].append(x)
    graph_bfs[x].append(y)
    graph_bfs[y].append(x)

for i in range(len(graph_dfs)):
    graph_dfs[i].sort()
    graph_bfs[i].sort()


visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph_dfs, start, visited_dfs)
print()
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph_bfs, start, visited_bfs)