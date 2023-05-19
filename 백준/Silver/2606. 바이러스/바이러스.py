from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n):
    graph[i].sort()

queue = deque([])

def bfs(graph, start, visited):
    queue.append(start)
    visited[start] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
cnt = 0
for i in range(1, len(visited)):
    if visited[i] == True:
        cnt += 1
print(cnt-1)