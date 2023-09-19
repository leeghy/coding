T = int(input())

li = []
for i in range(T):
    li.append(list(input()))

ans = []
for i in range(T):
    stack = []
    for j in li[i]:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                del stack[0]
    if len(stack) == 0:
        ans.append('YES')
    else:
        ans.append('NO')

for i in range(T):
    print(ans[i])
