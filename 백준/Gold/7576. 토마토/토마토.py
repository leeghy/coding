from collections import deque
N, M = map(int, input().split())

tomato = []
queue = deque([])

for i in range(M):
    tomato.append(list(map(int, input().split())))


for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            queue.append((i, j, 0))
p = 0
if len(queue) == 0:
    p = -1
    
def bfs(tomato):
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, v = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or ny <= -1 or nx >= M or ny >= N:
                continue
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                queue.append((nx, ny, v+1))
        
    return v

if p == -1:
    print(p)
else:
    s = 0
    a = bfs(tomato)

    for i in range(M):
        for j in range(N):
            if tomato[i][j] == 0:
                s = -1
                break

    if s != -1:
        print(a)
    else:
        print(s)