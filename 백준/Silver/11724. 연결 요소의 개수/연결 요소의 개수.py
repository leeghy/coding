from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([])

def bfs(graph, v, visited):
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

cnt = 0
for t in range(1, n+1):
    if visited[t] == False:
        bfs(graph, t, visited)
        cnt += 1

print(cnt)