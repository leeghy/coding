N = int(input())

li = []
for i in range(N):
    li.append(list(map(int, input().split())))

ans = []
count = 0
for i in range(N):
    for j in range(N):
        if li[j][0] > li[i][0] and li[j][1] > li[i][1]:
            count += 1
    ans.append(str(count+1))
    count = 0

a = " ".join(ans)
print(a)