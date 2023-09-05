N = int(input())

graph = [0]
for i in range(1, N+1):
    graph.append(int(input()))

def dfs(n, visited):
    if visited[n] == True:
        return n
    
    visited[n] = True
    return dfs(graph[n], visited)

li = []
for i in range(1, N+1):
    visited = [False] * (N+1)
    x = dfs(i, visited)
    if i == x:
        li.append(i)

print(len(li))
li.sort()
for i in li:
    print(i)