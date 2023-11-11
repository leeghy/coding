import sys
sys.setrecursionlimit(10**6)
column, row = map(int, input().split())

ans = []
field = []

for i in range(column):
    field.append(list(map(int, input().split())))

def dfs(x, y):
    global num
    if x <= -1 or y <= -1 or x >= row or y >= column:
        return False
    if field[y][x] == 0:
        return False
    if field[y][x] == 1:
        field[y][x] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        num += 1
        return True


paint_num = 0
for i in range(column):
    for j in range(row):
        if field[i][j] == 1:
            num = 0
            dfs(j, i)
            paint_num += 1
            ans.append(num)

if paint_num == 0:
    print(0)
    print(0)
else:
    print(paint_num)
    print(max(ans))