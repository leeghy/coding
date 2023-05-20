from collections import deque

n, m, h = map(int, input().split())

tomato = [[] for _ in range(h)]

for i in range(h):
    for j in range(m):
        tomato[i].append(list(map(int, input().split())))



queue = deque([])

def bfs(tomato):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    a = 0
    while queue:
        x, y, z, v = queue.popleft()
        a = v
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx <= -1 or ny <= -1 or nz <= -1 or nz >= h or ny >= m or nx >= n:
                continue
            if tomato[nz][ny][nx] == -1:
                continue
            if tomato[nz][ny][nx] == 1:
                continue
            if tomato[nz][ny][nx] == 0:
                queue.append((nx, ny, nz, v+1))
                tomato[nz][ny][nx] = 1
    return a

for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 1:
                queue.append((k, j, i, 0))
g = bfs(tomato)
ans = 0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 0:
                ans = -1
                break
if ans != -1:               
    print(g)
else:
    print(ans)
# print(tomato)

# if ans == 1:
#     ans -= 1
# print(ans)