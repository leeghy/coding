import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

li = [[] for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    li[x].append(y)
    li[y].append(x)

for i in range(1, n+1):
    li[i].sort()

visited = [False for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
def dfs(visited, tree, parent, kid, ans):

    if visited[kid] == True:
        return False

    visited[kid] = True
    ans[kid] = parent

    for i in tree[kid]:

        if visited[i] == True:
            continue
        dfs(visited, tree, kid, i, ans)
    return False

visited[0] = True
visited[1] = True
for i in li[1]:
    ans[i] = 1
    dfs(visited, li, 1, i, ans)

for i in range(2, n+1):
    print(ans[i])