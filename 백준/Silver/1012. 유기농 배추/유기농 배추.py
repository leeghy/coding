import sys
sys.setrecursionlimit(10**6)
t = int(input())
for q in range(t):
    n, m, k = map(int, sys.stdin.readline().split())

    graph = []
    for i in range(m):
        graph.append([0]*n)

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    
    def dfs(x, y):
        if x <= -1 or y <= -1 or x >= m or y >= n:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        else:
            return False

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    print(result)