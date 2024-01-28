T = int(input())

lst = []
for i in range(T):
    lst.append(list(map(int, input().split())))

dp = [[0] * 3 for i in range(T)]
dp[0] = lst[0]

for i in range(1, T):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + lst[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + lst[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + lst[i][2]

print(min(dp[T-1]))
