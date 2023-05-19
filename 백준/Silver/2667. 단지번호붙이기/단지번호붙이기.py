n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

li = []
num = 0
def dfs(x, y):
    global num
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1: 
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        li.append(num)
        return True
        

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
            ans.append(len(li))
            li = []

print(cnt)
ans.sort()
for i in range(len(ans)):
    print(ans[i])