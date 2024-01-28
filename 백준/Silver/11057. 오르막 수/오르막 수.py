N = int(input())

dp = [[0] * 10 for i in range(1001)]

dp[1] = [1]*10

for i in range(2, 1001):
    dp[i][0] = 1
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[N]) % 10007)