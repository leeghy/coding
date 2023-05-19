from collections import deque

n = int(input())

abnormal = [[] for _ in range(n)] #빨, 초 1, 파랑 0 
normal = [[] for _ in range(n)] #빨2 초록 1 파랑 0

for i in range(n):
    a = input()
    for j in range(n):
        if a[j] == 'R':
            abnormal[i].append(1)
            normal[i].append(2)
        elif a[j] == 'G':
            abnormal[i].append(1)
            normal[i].append(1)
        elif a[j] == 'B':
            abnormal[i].append(0)
            normal[i].append(0)

def bfs(graph, x, y, find):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or ny <= -1 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] != find:
                continue
            if graph[nx][ny] == find:
                queue.append((nx, ny))
                graph[nx][ny] = -1

        

        
cnt_ab = 0
cnt_nor = 0

for i in range(n):
    for j in range(n):
        if abnormal[i][j] != -1:
            bfs(abnormal, i, j, abnormal[i][j])
            cnt_ab += 1
        if normal[i][j] != -1:
            bfs(normal, i, j, normal[i][j])
            cnt_nor += 1

print(cnt_nor, cnt_ab)