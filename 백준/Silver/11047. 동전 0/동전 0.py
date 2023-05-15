N, K = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))
cnt = 0
li = list(reversed(li))
while K != 0:
    for i in li:
        if i <= K:
            cnt += K // i
            K -= (K//i)*i
print(cnt)