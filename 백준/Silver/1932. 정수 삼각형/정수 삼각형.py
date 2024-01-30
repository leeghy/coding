n = int(input())

dp = [[0] for _ in range(501)]
for i in range(1, n + 1):
    dp[i] = list(map(int, input().split()))

for i in range(2, n + 1):
    dp[i][0] += dp[i - 1][0]
    dp[i][i-1] += dp[i-1][i-2]
    for j in range(1, i-1):
        dp[i][j] = max(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j])

print(max(dp[n]))
