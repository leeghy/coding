import sys
sys.setrecursionlimit(10**6)

def dfs(map, x, y, width, height):
    if x <= -1 or y <= -1 or x >= width or y >= height:
        return False
    if map[y][x] == 0:
        return False
    map[y][x] = 0
    dfs(map, x, y-1, width, height)
    dfs(map, x, y+1, width, height)
    dfs(map, x-1, y, width, height)
    dfs(map, x+1, y, width, height)
    dfs(map, x-1, y-1, width, height)
    dfs(map, x-1, y+1, width, height)
    dfs(map, x+1, y-1, width, height)
    dfs(map, x+1, y+1, width, height)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    li = []
    for i in range(h):
        li.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if li[i][j] == 1:
                dfs(li, j, i, w, h)
                cnt += 1
    print(cnt)

