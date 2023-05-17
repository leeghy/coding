from collections import deque

queue = deque([])

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def bfs(graph):
    x = 0 
    y = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= M or nx <= -1 or ny <= -1:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
        

bfs(graph)
print(graph[N-1][M-1])