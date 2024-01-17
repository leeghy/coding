N = int(input())

p = list(map(int, input().split()))
p.insert(0, 0)

dp = [0] * (N + 1)
dp[1] = p[1]

for i in range(2, N + 1):
    tmp = []
    for j in range(i, -1, -1):
        tmp.append(p[j] + dp[i - j])
    dp[i] = max(tmp)

print(dp[N])
