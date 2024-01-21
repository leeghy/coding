N = int(input())

dp = [n for n in range(N + 1)]
M = int(N ** 0.5)

for i in range(2, M + 1):
    for j in range(i * i, N + 1):
        dp[j] = min(dp[j], dp[j - i * i] + 1)

print(dp[N])
